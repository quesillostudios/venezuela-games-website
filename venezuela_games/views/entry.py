from django.shortcuts import render
from ..models import VideoGame

def index(request):
    # Obtener los últimos 3 videojuegos añadidos
    latest_games = VideoGame.objects.all().order_by('-release_date')[:3]
    return render(request, 'index.html', {'latest_games': latest_games})