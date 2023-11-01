from fastapi import FastAPI
import models
from database import engine
import routes
import uvicorn

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(routes.router, tags=['create notification'], prefix='/api/note')


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
