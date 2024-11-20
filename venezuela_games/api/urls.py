from django.urls import path
from venezuela_games.views.entry import index
from venezuela_games.views.video_game import video_game_list, search_video_games, game_detail, search_video_games_ajax
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('video_games/', video_game_list, name='video_game_list'),
    path('video_games/search/', search_video_games, name='search_video_games'),
    path('video_games/<int:game_id>/', game_detail, name='game_detail'),
    path('search_video_games_ajax/', search_video_games_ajax, name='search_video_games_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])