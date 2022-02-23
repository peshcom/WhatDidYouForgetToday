#! /usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import v1


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
