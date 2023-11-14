import uvicorn

from database.seed import seed_database
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from router import index, deal

app = FastAPI()
seed_database()

app.include_router(index.router)
app.include_router(deal.router)

@app.get("/", include_in_schema=False, response_class=RedirectResponse)
async def root():
    return RedirectResponse(url="/docs", status_code=302)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
