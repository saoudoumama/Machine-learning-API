from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/medecins/", response_model=schemas.MedecinBase)
def create_medecin(medecin: schemas.MedecinBase, db: Session = Depends(get_db)):
    return crud.create_medecin(db,medecin)

@app.get("/medecins/", response_model=list[schemas.Medecin])
def read_medecins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list_medecins = crud.get_medecins(db, skip=skip, limit=limit)
    return list_medecins

@app.get("/specialites/", response_model=list[schemas.Speciality])
def read_specialities(db: Session = Depends(get_db)):
    list_specialities = crud.get_specialities(db)
    return list_specialities

@app.get("/{speciality}/medecins", response_model=list[schemas.Medecin])
def get_docs_by_speciality(speciality:int, db: Session = Depends(get_db)):
    list_medecins = crud.get_docs_by_speciality(speciality,db)
    return list_medecins  

@app.get("/cabinets/",response_model=list[schemas.Cabinet])
def get_cabinets(db: Session = Depends(get_db),skip: int = 0, limit: int = 100,):
    list_cabinets = crud.get_cabinets(db, skip=skip, limit=limit)
    return list_cabinets