# flask config
import os

DEBUG = True  # Turns on debugging features in Flask

# app config
DEXTR_IMAGE_FORM_DATA_KEY = "image"
DEXTR_IMAGE_UPLOAD_FOLDER = 'C://Users//scrat98//Documents//github//PencilMLBackend//web//upload'
DEXTR_IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(DEXTR_IMAGE_UPLOAD_FOLDER):
    os.makedirs(DEXTR_IMAGE_UPLOAD_FOLDER)
