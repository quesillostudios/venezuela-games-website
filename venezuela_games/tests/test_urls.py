from django.test import TestCase
from django.urls import reverse, resolve

from venezuela_games.models import Genre, VideoGame
from venezuela_games.views.entry import index
from venezuela_games.views.video_game import (
    video_game_list,
    search_video_games,
    game_detail,
    search_video_games_ajax,
)

class TestUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name="RPG")
        for i in range(1):
            game = VideoGame.objects.create(name=f"Game {i + 1}")
            game.genres.add(genre)

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_video_game_list_url_is_resolved(self):
        url = reverse('video_game_list')
        self.assertEqual(resolve(url).func, video_game_list)

    def test_search_video_games_url_is_resolved(self):
        url = reverse('search_video_games')
        self.assertEqual(resolve(url).func, search_video_games)

    def test_game_detail_url_is_resolved(self):
        url = reverse('game_detail', args=[1])  # El argumento es un ID ficticio
        self.assertEqual(resolve(url).func, game_detail)

    def test_search_video_games_ajax_url_is_resolved(self):
        url = reverse('search_video_games_ajax')
        self.assertEqual(resolve(url).func, search_video_games_ajax)

    def test_game_detail_url_with_valid_id(self):
        response = self.client.get(reverse('game_detail', args=[1]))  # ID ficticio
        self.assertEqual(response.status_code, 200)

    def test_game_detail_url_with_invalid_id(self):
        response = self.client.get(reverse('game_detail', args=[999]))  # ID inexistente
        self.assertEqual(response.status_code, 404)