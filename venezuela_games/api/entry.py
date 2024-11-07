from ninja import NinjaAPI
from ..models.videogame import VideoGame
from typing import List
from ninja.orm import create_schema

api = NinjaAPI()

VideoGameSchema = create_schema(VideoGame, exclude=['id'])

@api.get("/videogames", response=List[VideoGameSchema])
def list_videogames(request):
    return VideoGame.objects.all()

@api.post("/videogames", response=VideoGameSchema)
def create_videogame(request, data: VideoGameSchema):
    videogame = VideoGame.objects.create(**data.dict())
    return videogame

@api.get("/videogames/{id}", response=VideoGameSchema)
def get_videogame(request, id: int):
    return VideoGame.objects.get(id=id)