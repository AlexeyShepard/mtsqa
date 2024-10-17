from pydantic import BaseModel

class FormData(BaseModel):
    number: str
    name: str