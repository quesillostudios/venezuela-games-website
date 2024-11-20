from django.db import models
from venezuela_games.models.developer import Developer
from venezuela_games.models.game_engine import GameEngine
from venezuela_games.models.game_mode import GameMode
from venezuela_games.models.genre import Genre
from venezuela_games.models.theme import Theme

class VideoGame(models.Model):
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    themes = models.ManyToManyField(Theme)
    game_modes = models.ManyToManyField(GameMode)
    developers = models.ManyToManyField(Developer, related_name='developers')
    publishers = models.ManyToManyField(Developer, related_name='publishers')
    develop_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    game_engine = models.ForeignKey(GameEngine, on_delete=models.SET_NULL, null=True, blank=True)
    download_link = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name