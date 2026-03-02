from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FinBank Backend Running"}

@app.get("/balance")
def get_balance():
    return {"balance": 1000}
