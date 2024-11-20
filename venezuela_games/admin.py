from django.contrib import admin
from .models import VideoGame, Genre, GameEngine, Developer
from .models.video_game import Theme, GameMode


# Registro del modelo Genre
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GameMode)
class GameModeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registro del modelo GameEngine
@admin.register(GameEngine)
class GameEngineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registro del modelo Developer
@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'found_date')
    search_fields = ('name',)

# Registro del modelo VideoGame
@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'get_genres', 'game_engine', 'get_developers', 'get_publishers')
    search_fields = ('name', 'description')
    list_filter = ('release_date', 'game_engine', 'genres', 'developers')

    # Método personalizado para mostrar los géneros asociados al videojuego
    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    get_genres.short_description = 'Géneros'

    # Método personalizado para mostrar los desarrolladores asociados al videojuego
    def get_developers(self, obj):
        return ", ".join([developer.name for developer in obj.developers.all()])
    get_developers.short_description = 'Desarrolladores'

    def get_publishers(self, obj):
        return ", ".join([publisher.name for publisher in obj.publishers.all()])
    get_publishers.short_description = 'Publishers'