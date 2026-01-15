from fastapi import FastAPI, Request
from backend.services.logger import logger

app = FastAPI(title="Customer Record API")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Request completed: {response.status_code}")
    return response

@app.get("/")
def read_root():
    logger.info("Accessing root endpoint")
    return {"message": "Welcome to the Customer Record API"}
