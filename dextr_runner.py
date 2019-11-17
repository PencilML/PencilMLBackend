import os

from PIL import Image

from analitics.dextr import find_dextr_bit_mask


def main():
    # the mouth of the dog
    result = find_dextr_bit_mask(Image.open("images/dog-cat.jpg"), [[28, 205],
                                                                    [42, 209],
                                                                    [43, 187],
                                                                    [69, 193]])
    if not os.path.exists("images/dextr-results"):
        os.makedirs("images/dextr-results")

    result.bit_mask_image.save("images/dextr-results/dog-cat-mask-only.png")
    result.image_with_bit_mask.save("images/dextr-results/dog-cat-with-mask.png")


if __name__ == '__main__':
    main()
