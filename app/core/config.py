from pydantic_settings import BaseSettings

import torch

class Settings(BaseSettings):
    # PostgreSQL
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str  # no default
    POSTGRES_PORT: int 
   
    # MongoDB
    MONGO_DB: str
    MONGO_HOST: str
    MONGO_PORT: int

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    # FASTAPI / WebSocket PORTS
    FASTAPI_PORT: int
    WEBSOCKET_PORT: int
    NGROK_AUTH_TOKEN: str
    SECRET_KEY: str

    # Github
    GITHUB_TOKEN: str
    GITHUB_GIST_ID: str
    VITE_GITHUB_FETCH_URL_ROOT: str
    VITE_GITHUB_GIST_FILENAME: str

    # Torch
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"

    class Config:
        env_file = ".env"

settings = Settings()
