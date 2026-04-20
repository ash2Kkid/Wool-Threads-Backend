from fastapi import APIRouter, UploadFile, File
from app.services.fabric_service import analyze_fabric_mock
from app.database.fabric_db import save_fabric_check
from app.core.firebase import db

router = APIRouter(
    prefix="/fabric",
    tags=["Fabric Checker"]
)

@router.post("/check")
def check_fabric(
    user_id: str,
    image: UploadFile = File(...)
):
    result = analyze_fabric_mock()

    save_fabric_check(
        db=db,
        user_id=user_id,
        result=result
    )

    return result