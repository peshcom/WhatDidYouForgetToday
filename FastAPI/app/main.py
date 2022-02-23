#! /usr/bin/env python3

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from sqlalchemy.orm import Session

from .database import Base, get_db, engine
from .database.models import Users

from .api import v1


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="WhatDidYouForgetToday",
    description="TODO web application with FastAPI",
    version="0.0.1",

    contact={
        "name": "Peshcom",
        "url": "https://github.com/peshcom/WhatDidYouForgetToday",
    },

    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },

    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


# allow CORS headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# include additional routers
app.include_router(v1.router)


# Тестовый endpoint для проверки работоспособности
@app.get("/healcheck")
async def read_root():
    return {'status': True}


class UserCreate(BaseModel):
    login: str
    password: str


@app.post('/create_user')
async def index(user: UserCreate, db: Session = Depends(get_db)):
    """
    curl -X POST http://localhost/create_user -H "Content-Type: application/json" -d '{"login":"admin","password":"password"}'
    """
    def create_user(db: Session, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = Users(login=user.login, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    return create_user(db=db, user=user)


# действия при запуске и при завершении
@app.on_event("startup")
async def startup():
    """
    actions before start
    """
    pass


@app.on_event("shutdown")
async def shutdown():
    """
    actions after start
    """
    pass


# Very bad song, Fix this later
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=80, reload=True, debug=True)
