import json
import os
from datetime import datetime

import numpy as np
from PIL import Image
from flask import jsonify
from flask import request
from werkzeug.utils import secure_filename

from analitics.dextr import find_dextr_bit_mask
from web.app import app
from web.config import DEXTR_IMAGE_UPLOAD_FOLDER, DEXTR_IMAGE_ALLOWED_EXTENSIONS
from web.exceptions import BadRequest


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    return "Pong"


@app.route('/dextr-grayscale', methods=['POST'])
def dextr_algorithm_from_grayscale():
    data = json.loads(request.data)
    grayscale = data["grayscale"]
    extreme_points = data["extremePoints"]

    filename = f"grayscale_{datetime.utcnow().timestamp()}"
    file_path = os.path.join(DEXTR_IMAGE_UPLOAD_FOLDER, filename)
    img = Image.fromarray(np.array(grayscale, dtype=np.uint8), "L").convert("RGB")
    img.save(f"{file_path}.jpg")

    dextr_result = find_dextr_bit_mask(img, extreme_points)
    dextr_result.bit_mask_image.save(f"{file_path}_bit_mask_only.png")
    dextr_result.image_with_bit_mask.save(f"{file_path}_image_with_bit_mask.png")

    return jsonify(dextr_result.bit_mask_array.tolist())


@app.route('/dextr-image', methods=['POST'])
def dextr_algorithm_from_image():
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in DEXTR_IMAGE_ALLOWED_EXTENSIONS

    def get_image_from_request():
        if "image" not in request.files:
            raise BadRequest('No file part')
        file = request.files["image"]

        if file.filename == '':
            raise BadRequest('No selected file')

        if not file or not allowed_file(file.filename):
            raise BadRequest(f"Not allowed file extension. Supported formats: {DEXTR_IMAGE_ALLOWED_EXTENSIONS}")

        return file

    def get_extreme_points_from_request():
        if "extremePoints" not in request.form:
            raise BadRequest('No extremePoints provided')
        points = json.loads(request.form["extremePoints"])

        if len(points) != 4:
            raise BadRequest("Excepted 4 points")

        for point in points:
            if len(point) != 2:
                raise BadRequest("Point should consists 2 integers")

        return points

    image_file = get_image_from_request()
    extreme_points = get_extreme_points_from_request()

    filename = f"{datetime.utcnow().timestamp()}_{secure_filename(image_file.filename)}"
    file_path = os.path.join(DEXTR_IMAGE_UPLOAD_FOLDER, filename)
    image_file.save(file_path)

    image = Image.open(file_path)
    dextr_result = find_dextr_bit_mask(image, extreme_points)
    dextr_result.bit_mask_image.save(f"{file_path}_bit_mask_only.png")
    dextr_result.image_with_bit_mask.save(f"{file_path}_image_with_bit_mask.png")

    return jsonify(dextr_result.bit_mask_array.tolist())
