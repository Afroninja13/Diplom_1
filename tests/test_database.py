import pytest
from praktikum.database import Database


class TestDatabase:

    def setup_method(self):
        self.database = Database()

    @pytest.mark.parametrize('index, name, price', [
        (0, 'black bun', 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ])
    def test_available_buns_returns_correct_list(self, index, name, price):
        """
        Функция available_buns возвращает корректный список buns
        """
        assert self.database.available_buns()[index].name == name
        assert self.database.available_buns()[index].price == price

    @pytest.mark.parametrize('index, name, price', [
        (0, 'hot sauce', 100),
        (1, "sour cream", 200),
        (2, "chili sauce", 300),
        (3, 'cutlet', 100),
        (4, "dinosaur", 200),
        (5, "sausage", 300)
    ])
    def test_available_ingredients_returns_correct_list(self, index, name, price):
        """
        Функция available_ingredients возвращает корректный список ingredients
        """
        assert self.database.available_ingredients()[index].name == name
        assert self.database.available_ingredients()[index].price == price
