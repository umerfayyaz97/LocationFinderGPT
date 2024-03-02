from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated

app = FastAPI(
    title="Location Finder API",
    version="1.0.0",
    description="API to find the location of a given address",
    servers=[{
        "url": "",
        "description":"Development Server"
    }]
)