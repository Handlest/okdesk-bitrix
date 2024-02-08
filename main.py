from fastapi import FastAPI
from config import Base, engine
from routers.okdesk_routes import okdesk_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(okdesk_router)
