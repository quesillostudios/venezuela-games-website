# games/views.py
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from ..models.videogame import VideoGame

# Vista para mostrar la lista de videojuegos
def videogame_list(request):
    # Obtener el filtro de letra, si se proporciona en los parámetros de consulta
    letter = request.GET.get('letter', '')

    # Filtrar los videojuegos por la primera letra del nombre
    if letter == '0':  # Números
        games = VideoGame.objects.filter(name__regex=r'^[0-9]').order_by('name')
    elif letter == '#':  # Símbolos
        games = VideoGame.objects.filter(name__regex=r'^[^A-Za-z0-9]').order_by('name')
    elif letter:  # Letra específica
        games = VideoGame.objects.filter(name__istartswith=letter).order_by('name')
    else:  # Sin filtro
        games = VideoGame.objects.all().order_by('name')

    paginator = Paginator(games, 20)  # Paginación de 20 elementos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'videogames/videogame_list.html', {'page_obj': page_obj, 'letter': letter})

# Vista de búsqueda de videojuegos
def search_videogames(request):
    query = request.GET.get('query', '')
    if query:
        # Filtra por el nombre o por géneros relacionados
        videogames = VideoGame.objects.filter(
            Q(name__icontains=query) |
            Q(genres__name__icontains=query)
        ).distinct()  # Usa distinct para evitar duplicados en relaciones M2M
    else:
        videogames = VideoGame.objects.none()

    return render(request, 'videogames/search.html', {'query': query, 'videogames': videogames})

# Vista de detalles del videojuego
def game_detail(request, game_id):
    game = get_object_or_404(VideoGame, id=game_id)
    return render(request, 'videogames/game_detail.html', {'game': game})

def search_videogames_ajax(request):
    query = request.GET.get('query', '')
    games = VideoGame.objects.filter(name__icontains=query)[:10]  # Limitar a los primeros 10 resultados
    results = [{"id": game.id, "name": game.name} for game in games]
    return JsonResponse(results, safe=False)