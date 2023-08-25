from fastapi import FastAPI
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi.middleware.cors import CORSMiddleware
from Services import songsService
from Services import recommenderService


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

currentDatasetPath = "Data/embeddingK128_R300_B4096/"

@app.get("/")
async def index():
    return songsService.getSongsForSeachBar(currentDatasetPath)

@app.get("/recommenderService/{id}")
async def getData(id: int):
    return recommenderService.Recommend(currentDatasetPath, id)

asyncio.run(serve(app, Config()))