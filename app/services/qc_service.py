from ml.quality_control.src.predict import WoolPredictor
import os
import requests

# -------------------------------
# CONFIG
# -------------------------------

# 🔴 Replace this with your actual model download link
MODEL_URL = "https://drive.google.com/uc?export=download&id=1mtr68e9bB-JPqn_4t04sYm8s9kNR9UsY"

# Local dev path (outside repo)
LOCAL_MODEL_PATH = os.path.abspath(
    "../ml/quality_control/models/efficientnet_20260208_102749/best_model.h5"
)

# Production path (inside server/container)
PROD_MODEL_PATH = os.path.join(
    "models",
    "best_model.h5"
)

# -------------------------------
# SINGLETON INSTANCE
# -------------------------------

_predictor = None


# -------------------------------
# MODEL PATH HANDLER
# -------------------------------

def get_model_path():
    """
    Returns correct model path based on environment
    """

    # 1. Local development (preferred)
    if os.path.exists(LOCAL_MODEL_PATH):
        print("Using local ML model")
        return LOCAL_MODEL_PATH

    # 2. Already downloaded (production cache)
    if os.path.exists(PROD_MODEL_PATH):
        print("Using cached model")
        return PROD_MODEL_PATH

    # 3. Download model if not found
    print("Downloading model...")
    download_model(PROD_MODEL_PATH)

    return PROD_MODEL_PATH


# -------------------------------
# DOWNLOAD FUNCTION
# -------------------------------

def download_model(save_path):
    """
    Downloads model from external storage
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    response = requests.get(MODEL_URL, stream=True)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Model downloaded successfully")


# -------------------------------
# PREDICTOR LOADER
# -------------------------------

def get_predictor():
    """
    Loads model only once (singleton)
    """
    global _predictor

    if _predictor is None:
        model_path = get_model_path()

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")

        print(f"Loading model from: {model_path}")
        _predictor = WoolPredictor(model_path)

    return _predictor


# -------------------------------
# INFERENCE FUNCTION
# -------------------------------

def run_quality_check(image_path: str):
    """
    Runs prediction using image path
    """
    predictor = get_predictor()
    return predictor.predict_api(image_path)