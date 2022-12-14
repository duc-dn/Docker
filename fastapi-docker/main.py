from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello world"}

@app.get("items/{item_id}")
async def get_items(item_id: int):
    return {"item_id": item_id}