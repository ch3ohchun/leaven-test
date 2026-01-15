from fastapi import FastAPI

app = FastAPI(title="Customer Record API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Record API"}
