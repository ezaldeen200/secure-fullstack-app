from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Task

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Task Manager")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Secure Task Manager API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.post("/tasks")
def create_task(task: dict, db: Session = Depends(get_db)):
    new_task = Task(
        title=task["title"],
        completed=False,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    return {"message": "Task deleted"}
