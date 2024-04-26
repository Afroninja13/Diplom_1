import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize('price', [
        -1.0,
        0,
        2.2250738585072014e-308,
        1.7976931348623157e+308
    ])
    def test_get_price_returns_correct_value(self, price):
        """
        Проверка функции get_price. Возвращает значение price с которым создан экземпляр класса Ingredient
        """
        ingredient = Ingredient('SAUSE', 'test', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('name', [
        '',
        None,
        'veryLongStringVeryLongStringVeryLongStringVeryLongStringVeryLongString',
        '`()!@#$%^&*[]{}|;:",./.,?><'
    ])
    def test_get_name_returns_correct_value(self, name):
        """
        Проверка функции get_name. Возвращает значение name с которым создан экземпляр класса Ingredient
        """
        ingredient = Ingredient('SAUSE', name, 20.0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type', [
        'SAUSE',
        'FILLING',
    ])
    def test_get_type_returns_correct_value(self, ingredient_type):
        """
        Проверка функции get_type. Возвращает значение type с которым создан экземпляр класса Ingredient
        """
        ingredient = Ingredient(ingredient_type, 'test', 20.0)
        assert ingredient.get_type() == ingredient_type
