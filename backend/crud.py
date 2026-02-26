from sqlalchemy.orm import Session
from sqlalchemy import case
import models
import schemas

def get_patients(db: Session):
    priority_order = case(
        (models.Patient.priority == "Critical", 1),
        (models.Patient.priority == "Moderate", 2),
        (models.Patient.priority == "Routine", 3),
        else_=4
    )
    return db.query(models.Patient).order_by(priority_order, models.Patient.check_in_time.asc()).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient