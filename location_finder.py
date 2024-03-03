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

#creating pydantic class
class Location(BaseModel):
    name: str
    address: str

#Dummy Data

locations = {
    "umer":Location(name="umer", address="Lahore"),
    "ali":Location(name="ali", address="Islamabad"),
}

#dependency Function
def get_Location_or_404(name: str)->Location:
    loc = locations.get(name.lower())
    if not loc: 
        raise HTTPException(status_code=404, detail=f"Location not found for {name}")
    return loc

#routes

@app.get("/location/{name}")
def get_person_location(name: str, location: Annotated[Location, Depends(get_Location_or_404)]):
    return location


