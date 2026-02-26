from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas
import crud
import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="CareQueue API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://carequeue-gilt.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/patients", response_model=list[schemas.Patient])
def get_patients(db: Session = Depends(database.get_db)):
    return crud.get_patients(db)

@app.post("/patients", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(database.get_db)):
    return crud.create_patient(db, patient)

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(database.get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not patient:
            raise HTTPException(status_code=404, detail="Patient record not found")

    db.delete(patient)
    db.commit()
    return {"status": "success", "message": "Patient {patient_id} deleted successfully!"}