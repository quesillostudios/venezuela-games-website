from django.test import TestCase
from venezuela_games.models.video_game import Genre, VideoGame


class TestModels(TestCase):
    def test_genre_str(self):
        genre = Genre.objects.create(name="Action")
        self.assertEqual(str(genre), "Action")

    def test_video_game_genres_relationship(self):
        genre = Genre.objects.create(name="Action")
        game = VideoGame.objects.create(name="Test Game")
        game.genres.add(genre)

        self.assertEqual(game.genres.count(), 1)
        self.assertIn(genre, game.genres.all())
