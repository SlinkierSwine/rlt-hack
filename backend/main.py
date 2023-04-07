import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.routes.router import router
import logging


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "ok"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
