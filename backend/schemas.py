from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PatientBase(BaseModel):
    name: str
    symptoms: str
    priority: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    check_in_time: datetime