import uvicorn
from fastapi import FastAPI

from database.database import engine
from database.models import Base
from handlers import routers

Base.metadata.create_all(bind=engine)

app = FastAPI()
for router in routers:
    app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
