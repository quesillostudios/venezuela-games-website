from django.test import TestCase
from django.urls import reverse
from venezuela_games.models.video_game import VideoGame
from venezuela_games.models.genre import Genre

class VideoGameListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre = Genre.objects.create(name="Action")
        for i in range(3):
            game = VideoGame.objects.create(name=f"Game {i + 1}")
            game.genres.add(genre)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/video_games/')  # Ajusta el URL según tu configuración
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('video_game_list'))  # Ajusta el nombre de la vista
        self.assertTemplateUsed(response, 'video_games/video_game_list.html')

    def test_view_filters_by_letter(self):
        response = self.client.get(reverse('video_game_list') + '?letter=G')
        self.assertContains(response, 'Game 1')
        self.assertContains(response, 'Game 2')
        self.assertContains(response, 'Game 3')

    def test_view_pagination(self):
        response = self.client.get(reverse('video_game_list') + '?page=1')
        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 3)  # Verifica cantidad en la página

    def test_pagination_in_video_game_list(self):
        for i in range(25):  # Crear más videojuegos
            VideoGame.objects.create(name=f"Game {i + 1}")

        response = self.client.get(reverse('video_game_list') + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 20)  # Primera página con 20 elementos

        response = self.client.get(reverse('video_game_list') + '?page=2')
        self.assertEqual(len(response.context['page_obj']), 8)  # Segunda página con 5 elementos restantes + los 3 inciales

    def test_filter_video_games_by_genre(self):
        action_genre = Genre.objects.create(name="Horror")
        adventure_genre = Genre.objects.create(name="Adventure")
        game1 = VideoGame.objects.create(name="Game 1")
        game2 = VideoGame.objects.create(name="Game 2")
        game1.genres.add(action_genre)
        game2.genres.add(adventure_genre)

        response = self.client.get(reverse('video_game_list') + '?genre=Horror')
        self.assertContains(response, 'Game 1')
        self.assertNotContains(response, 'Game 2')

    def test_search_video_games_ajax_response_format(self):
        VideoGame.objects.create(name="Super Mario")
        response = self.client.get(reverse('search_video_games_ajax') + '?query=Mario')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_search_video_games_ajax_no_results(self):
        response = self.client.get(reverse('search_video_games_ajax') + '?query=UnknownGame')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [])



