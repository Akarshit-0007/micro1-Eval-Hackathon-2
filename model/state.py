from pydantic import BaseModel
from typing import List, Optional

class InputState(BaseModel):
    input: str
    files: Optional[List[str]] = None

class OutputState(BaseModel):
    output: Optional[str] = None  # Gives it a default so it's not strictly required at initialization

class OverAllState(InputState, OutputState):
    pass