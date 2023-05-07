from fastapi import FastAPI
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi.middleware.cors import CORSMiddleware
import recommender
import songsData

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://192.168.1.102:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return songsData.getSongsForSeachBar()

@app.get("/SearchBar")
async def root():
    return {}

@app.post("/")
async def root():
    return recommender.Recommend()

asyncio.run(serve(app, Config()))