import pytest
from one_hot_encoder import fit_transform


def test_cities_example():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == expected


def test_string_args():
    expected = [
        ('a', [0, 1]),
        ('b', [1, 0]),
        ('a', [0, 1]),
    ]
    assert fit_transform('a', 'b', 'a') == expected


def test_empty_list_input():
    assert fit_transform([]) == []


def test_all_unique_items():
    data = ['A', 'B', 'C']
    expected = [
        ('A', [0, 0, 1]),
        ('B', [0, 1, 0]),
        ('C', [1, 0, 0]),
    ]
    assert fit_transform(data) == expected


def test_raises_exception_on_no_args():
    with pytest.raises(TypeError):
        fit_transform()
