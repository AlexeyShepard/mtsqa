from pydantic import BaseModel
from typing import Optional

class InverseData(BaseModel):
    key1: Optional[str] = None