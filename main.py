from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, get_db


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/tracks")
def get_tracks(db: Session = Depends(get_db)):
    return db.query(models.Track).all()

@app.post("/tracks")
def create_track(track: dict, db: Session = Depends(get_db)):
    db_track = models.Track(**track)
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track


@app.get("/tracks/{id}")
def get_track(id: int, db: Session = Depends(get_db)):
    return db.query(models.Track).filter(models.Track.id == id).first()


@app.put("/tracks/{id}")
def update_track(id: int, updated: dict, db: Session = Depends(get_db)):
    db_track = db.query(models.Track).filter(models.Track.id == id).first()
    if not db_track:
        return {"error": "Not found"}
    for key, value in updated.items():
        setattr(db_track, key, value)
    db.commit()
    db.refresh(db_track)
    return db_track

@app.delete("/tracks/{id}")
def delete_track(id: int, db: Session = Depends(get_db)):
    db_track = db.query(models.Track).filter(models.Track.id == id).first()
    if not db_track:
        return {"error": "Not found"}
    db.delete(db_track)
    db.commit()
    return {"message": "deleted"}