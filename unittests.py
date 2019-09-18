from app import app
from tenor import gif_search, get_popular_gifs, get_random_gifs
import unittest


class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        print(result)

        self.assertEqual(result.status_code, 200)

    def test_gif_search_query(self):
        pass

    def test_get_popular_gifs():
        pass

    def test_get_random_gifs(self):
        pass


if __name__ == '__main__':
    unittest.main()
