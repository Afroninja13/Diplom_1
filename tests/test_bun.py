import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', [
        '',
        None,
        'veryLongStringVeryLongStringVeryLongStringVeryLongStringVeryLongString',
        '`()!@#$%^&*[]{}|;:",./.,?><'
    ])
    def test_get_name_returns_correct_value(self, name):
        """
        Проверка функции get_name. Возвращает значение name с которым создан экземпляр класса Bun
        """
        bun = Bun(name, 20.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [
        -1.0,
        0,
        2.2250738585072014e-308,
        1.7976931348623157e+308
    ])
    def test_get_price_returns_correct_value(self, price):
        """
        Проверка функции get_price. Возвращает значение price с которым создан экземпляр класса Bun
        """
        bun = Bun('test', price)
        assert bun.get_price() == price
