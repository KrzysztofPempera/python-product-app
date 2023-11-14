import uvicorn

from database.seed import seed_database
from fastapi import FastAPI
from router import index, deal

app = FastAPI()
seed_database()

app.include_router(index.router)
app.include_router(deal.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
