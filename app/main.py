import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, Query
from fastapi.concurrency import asynccontextmanager
from typing import Optional
from prisma import Prisma

from view import routers
from model.connect_to_db import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    if db.is_connected():
        await db.disconnect()


app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
