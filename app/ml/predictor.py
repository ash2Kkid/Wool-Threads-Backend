import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import load_img, img_to_array
import requests

# -------------------------------
# CONFIG
# -------------------------------

IMG_SIZE = (224, 224)
CLASSES = ["Bad", "Good"]  # adjust if needed

MODEL_PATH = "models/best_model.h5"
MODEL_URL = os.getenv("MODEL_URL")  # set in Railway


class WoolPredictor:
    def __init__(self):
        self.model = None

    def load_model(self):
        if self.model is not None:
            return self.model

        # Create models folder
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

        # Download model if not exists
        if not os.path.exists(MODEL_PATH):
            if not MODEL_URL:
                raise ValueError("MODEL_URL environment variable not set")

            print("Downloading model...")
            response = requests.get(MODEL_URL, stream=True)
            response.raise_for_status()

            with open(MODEL_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            print("Model downloaded")

        print("Loading model...")
        self.model = tf.keras.models.load_model(MODEL_PATH, compile=False)
        print("Model loaded successfully")

        return self.model

    def preprocess_image(self, image_path):
        img = load_img(image_path, target_size=IMG_SIZE)
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, image_path: str):
        model = self.load_model()

        img_array = self.preprocess_image(image_path)
        preds = model.predict(img_array, verbose=0)[0]

        idx = int(np.argmax(preds))
        confidence = float(preds[idx])

        return {
            "quality": CLASSES[idx],
            "confidence": round(confidence, 4),
            "probabilities": {
                CLASSES[i]: round(float(preds[i]), 4)
                for i in range(len(CLASSES))
            }
        }


# ✅ Singleton instance (VERY IMPORTANT)
predictor = WoolPredictor()