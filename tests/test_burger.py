from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:

    mock_bun = Mock()
    mock_bun.configure_mock(name='bun', price=20.0)

    mock_ingredient = Mock()
    mock_ingredient.configure_mock(type='SAUSE', name='ingredient', price=20.0)

    mock_ingredient2 = Mock()
    mock_ingredient2.configure_mock(type='FILLING', name='ingredient2', price=10.0)

    def setup_method(self):
        self.burger = Burger()

    def test_set_buns_adds_correct_bun(self):
        """
        Функция set_buns добавляет объект bun c корректными полями name и price
        """
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun.name == 'bun'
        assert self.burger.bun.price == 20.0

    def test_add_ingredient_adds_correct_ingredient(self):
        """
        Функция add_ingredient добавляет ингредиент с корректными полями name, type, price
        """
        self.burger.add_ingredient(self.mock_ingredient)
        assert self.burger.ingredients[0].name == 'ingredient'
        assert self.burger.ingredients[0].type == 'SAUSE'
        assert self.burger.ingredients[0].price == 20.0

    def test_add_ingredient_appends_new_element_in_list(self):
        """
        Функция add_ingredient добавляет новый элемент в список ingredients
        """
        self.burger.add_ingredient(self.mock_ingredient)
        assert len(self.burger.ingredients) == 1

    def test_remove_ingredient_removes_element_from_list(self):
        """
        Функция remove_ingredient удаляет элемент из списка ingredients
        """
        self.burger.add_ingredient(self.mock_ingredient)
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 0

    def test_move_ingredient_moves_element_correct(self):
        """
        Функция move_ingredient перемещает элемент в заданное место списка
        """
        self.burger.add_ingredient(self.mock_ingredient)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0].name == 'ingredient2' and self.burger.ingredients[1].name == 'ingredient'

    def test_get_price_returns_correct_value(self):
        """
        Функция get_price возвращает корректную общую стоимость булочек и ингредиентов
        """
        self.mock_bun.get_price.return_value = 20.0
        self.mock_ingredient.get_price.return_value = 20.0
        self.mock_ingredient2.get_price.return_value = 10.0

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient)
        self.burger.add_ingredient(self.mock_ingredient2)
        assert self.burger.get_price() == 70

    def test_get_reciept_returns_correct_value(self):
        """
        Функция get_reciept возвращает корректный список ингредиентов заказа
        """
        self.mock_bun.get_name.return_value = 'bun'
        self.mock_ingredient.get_type.return_value = 'SAUSE'
        self.mock_ingredient.get_name.return_value = 'ingredient'
        self.mock_bun.get_price.return_value = 20.0
        self.mock_ingredient.get_price.return_value = 20.0

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient)
        assert self.burger.get_receipt() == '(==== bun ====)\n= sause ingredient =\n(==== bun ====)\n\nPrice: 60.0'
