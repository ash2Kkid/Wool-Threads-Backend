from pydantic import BaseModel

class FabricResult(BaseModel):
    pattern: str
    quality: str
    confidence: float