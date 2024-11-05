from fastapi import FastAPI
from app.config.db import check_connection
from app.routes.productRoutes import router as products_router
app = FastAPI()

async def lifespan(app: FastAPI):
    check_connection()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI product API"}

app.include_router(products_router)
