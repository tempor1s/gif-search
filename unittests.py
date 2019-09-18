from app import app
from tenor import gif_search, get_popular_gifs, get_random_gifs
import unittest


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200,
                         "Status code is not 200.  Not sucessful get.")

    def test_gif_search_query(self):  # Test for search condition
        result = self.app.get(
            '/', query_string=dict(type='search', query='test'))
        self.assertEqual(result.status_code, 200,
                         'Search functionality does not return status code of 200')

    def test_get_popular_gifs(self):  # Test for popular gif condition
        result = self.app.get('/', query_string=dict(type='popular'))
        self.assertEqual(result.status_code, 200,
                         'Popular gifs does not return status code of 200')

    def test_get_random_gifs(self):  # Test for random gif condition
        result = self.app.get('/', query_string=dict(type='random'))
        self.assertEqual(result.status_code, 200,
                         'Random gifs do not return status code of 200')


class FunctionTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_gif_search(self):
        result = gif_search('test')

        self.assertNotEqual(len(result), 0, 'Gif search test failed')

    def test_popular_gifs(self):
        result = get_popular_gifs()

        self.assertNotEqual(len(result), 0, 'Popular search test failed')

    def test_random_gifs(self):
        result = get_random_gifs()

        self.assertNotEqual(len(result), 0, 'Random gif search failed')


if __name__ == '__main__':
    unittest.main()
