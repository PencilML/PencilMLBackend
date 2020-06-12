import os

import numpy as np
import torch
from PIL import Image
from torch.nn.functional import upsample

from . import resnet, helpers
from .config import MODELS_DIR, USE_GPU, MODEL_NAME, GPU_ID, PAD, THRESHOLD
from .helpers import make_masks_image, add_mask_to_the_image

if USE_GPU:
    print(f"Try to use GPU with id {GPU_ID}")
    device = torch.device("cuda:" + str(GPU_ID) if torch.cuda.is_available() else "cpu")
else:
    print(f"Use CPU")
    device = torch.device("cpu")

#  Create the network and load the weights
net = resnet.resnet101(1, nInputChannels=4, classifier='psp')
modelFilePath = os.path.join(MODELS_DIR, MODEL_NAME + '.pth')
print(f"Initializing weights from: {modelFilePath}")
state_dict_checkpoint = torch.load(os.path.join(MODELS_DIR, MODEL_NAME + '.pth'),
                                   map_location=lambda storage, loc: storage)
net.load_state_dict(state_dict_checkpoint)
net.eval()
net.to(device)


def find_dextr_bit_mask(image_file, extreme_points_double_array):
    image = np.array(image_file)
    extreme_points = np.array(extreme_points_double_array)

    #  Crop image to the bounding box from the extreme points and resize
    bbox = helpers.get_bbox(image, points=extreme_points, pad=PAD, zero_pad=True)
    crop_image = helpers.crop_from_bbox(image, bbox, zero_pad=True)
    resize_image = helpers.fixed_resize(crop_image, (512, 512)).astype(np.float32)

    #  Generate extreme point heat map normalized to image values
    extreme_points = extreme_points - [np.min(extreme_points[:, 0]), np.min(extreme_points[:, 1])] + [PAD, PAD]
    extreme_points = (512 * extreme_points * [1 / crop_image.shape[1], 1 / crop_image.shape[0]]).astype(np.int)
    extreme_heatmap = helpers.make_gt(resize_image, extreme_points, sigma=10)
    extreme_heatmap = helpers.cstm_normalize(extreme_heatmap, 255)

    #  Concatenate inputs and convert to tensor
    input_dextr = np.concatenate((resize_image, extreme_heatmap[:, :, np.newaxis]), axis=2)
    inputs = torch.from_numpy(input_dextr.transpose((2, 0, 1))[np.newaxis, ...])

    # Run a forward pass
    inputs = inputs.to(device)
    outputs = net.forward(inputs)
    outputs = upsample(outputs, size=(512, 512), mode='bilinear', align_corners=True)
    outputs = outputs.to(torch.device('cpu'))

    pred = np.transpose(outputs.data.numpy()[0, ...], (1, 2, 0))
    pred = 1 / (1 + np.exp(-pred))
    pred = np.squeeze(pred)

    # Make the mask result
    bit_mask_array = helpers.crop2fullmask(pred, bbox, im_size=image.shape[:2], zero_pad=True, relax=PAD) > THRESHOLD
    bit_mask_image = make_masks_image([bit_mask_array])
    image_with_bit_mask = add_mask_to_the_image(image_file, bit_mask_image)

    return DextrAlgorithmResult(
        bit_mask_array=bit_mask_array,
        bit_mask_image=bit_mask_image,
        image_with_bit_mask=image_with_bit_mask
    )


class DextrAlgorithmResult:
    bit_mask_array: [[]] = [[]]
    bit_mask_image: Image = Image.Image
    image_with_bit_mask: Image = Image.Image

    def __init__(self, bit_mask_array: [[]], bit_mask_image: Image, image_with_bit_mask: Image):
        self.bit_mask_array = bit_mask_array
        self.bit_mask_image = bit_mask_image
        self.image_with_bit_mask = image_with_bit_mask
