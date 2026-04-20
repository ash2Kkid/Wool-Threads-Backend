from app.ml.predictor import predictor

def run_quality_check(image_path: str):
    """
    Runs prediction using image path
    """
    return predictor.predict(image_path)