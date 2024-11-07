from django.db import models

# Modelo de Género
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Modelo de Game Engine
class GameEngine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class VideoGame(models.Model):
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)  # Relación de varios géneros
    release_date = models.DateField()
    game_engine = models.ForeignKey(GameEngine, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con un solo Game Engine
    download_link = models.URLField(max_length=200, blank=True, null=True)
    developers = models.ManyToManyField(Developer)  # Relación de varios desarrolladores
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
