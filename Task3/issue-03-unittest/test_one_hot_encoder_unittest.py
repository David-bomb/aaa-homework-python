import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):

    def test_cities_example(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), expected)

    def test_single_argument(self):
        fruits = ['apple', 'apple', 'apple']
        expected = [('apple', [1]), ('apple', [1]), ('apple', [1])]
        self.assertEqual(fit_transform(fruits), expected)

    def test_no_repeats(self):
        items = ['a', 'b', 'c']
        expected = [
            ('a', [0, 0, 1]),
            ('b', [0, 1, 0]),
            ('c', [1, 0, 0]),
        ]
        actual = fit_transform(items)
        self.assertEqual(actual, expected)
        # Проверяем, что 'd' не является ключом в результатах
        all_keys = {item[0] for item in actual}
        self.assertNotIn('d', all_keys)

    def test_empty_list_input(self):
        self.assertEqual(fit_transform([]), [])

    def test_exception_on_no_arguments(self):
        with self.assertRaises(TypeError):
            fit_transform()
