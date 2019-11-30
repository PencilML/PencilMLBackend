# flask config
import os

DEBUG = os.environ.get("PENCIL_ML_WEB_DEBUG", True)  # Turns on debugging features in Flask

# app config
DEXTR_IMAGE_FORM_DATA_KEY = "image"
DEXTR_IMAGE_UPLOAD_FOLDER = os.environ.get("PENCIL_ML_WEB_DEXTR_IMAGE_UPLOAD_FOLDER")
DEXTR_IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(DEXTR_IMAGE_UPLOAD_FOLDER):
    os.makedirs(DEXTR_IMAGE_UPLOAD_FOLDER)
