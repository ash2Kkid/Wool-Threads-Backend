from fastapi import APIRouter, UploadFile, File
import uuid, os, shutil
from app.services.qc_service import run_quality_check

router = APIRouter(prefix="/quality", tags=["Quality Control"])


@router.post("/check")
async def check_quality(image: UploadFile = File(...)):
    os.makedirs("tmp", exist_ok=True)

    path = f"tmp/{uuid.uuid4()}.jpg"

    try:
        # Save file temporarily
        with open(path, "wb") as f:
            shutil.copyfileobj(image.file, f)

        # Run prediction
        result = run_quality_check(path)

        return result

    finally:
        # Always cleanup (even if error occurs)
        if os.path.exists(path):
            os.remove(path)