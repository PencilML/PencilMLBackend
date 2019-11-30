import os

MODELS_DIR = os.environ.get("PENCIL_ML_ANALYTICS_MODELS_DIR")
MODEL_NAME = os.environ.get("PENCIL_ML_ANALYTICS_MODEL_NAME", "dextr_pascal-sbd")
USE_GPU = os.environ.get("PENCIL_ML_ANALYTICS_USE_GPU", True)
PAD = os.environ.get("PENCIL_ML_ANALYTICS_PAD", 50)
THRESHOLD = os.environ.get("PENCIL_ML_ANALYTICS_THRESHOLD", 0.8)
GPU_ID = os.environ.get("PENCIL_ML_ANALYTICS_THRESHOLD", 0)
