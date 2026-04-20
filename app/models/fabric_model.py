from pydantic import BaseModel

class FabricCheckRequest(BaseModel):
    # Image is sent as multipart, so this stays empty for now
    pass