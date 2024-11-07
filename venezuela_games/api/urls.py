from django.urls import path
from venezuela_games.views.entry import index
from venezuela_games.views.videogame import videogame_list, search_videogames, game_detail, search_videogames_ajax
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('videogames/', videogame_list, name='videogame_list'),
    path('videogames/search/', search_videogames, name='search_videogames'),
    path('videogames/<int:game_id>/', game_detail, name='game_detail'),
    path('search_videogames_ajax/', search_videogames_ajax, name='search_videogames_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])