from ninja import NinjaAPI
from ..models.video_game import VideoGame
from typing import List
from ninja.orm import create_schema

api = NinjaAPI()

VideoGameSchema = create_schema(VideoGame, exclude=['id'])

@api.get("/video_games", response=List[VideoGameSchema])
def list_video_games(request):
    return VideoGame.objects.all()

@api.post("/video_games", response=VideoGameSchema)
def create_video_game(request, data: VideoGameSchema):
    video_game = VideoGame.objects.create(**data.dict())
    return video_game

@api.get("/video_games/{id}", response=VideoGameSchema)
def get_video_game(request, id: int):
    return VideoGame.objects.get(id=id)