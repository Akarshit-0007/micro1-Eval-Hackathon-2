from typing import Optional, List
from pydantic import BaseModel

class OverAllState(BaseModel):
    input: str = ""
    files: Optional[List[str]] = None
    contain_files: Optional[bool] = None
    output: Optional[str] = None