from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_create_menu(self):
        # create a new menu object
        menu = Menu.objects.create(name='Lunch', price=20, description='A selection of Lunch items')

        # check that the string representation of the object is as expected
        self.assertEqual(str(menu), 'Lunch : A selection of Lunch items')

        # check that the name, price, and description fields are set correctly
        self.assertEqual(menu.name, 'Lunch')
        self.assertEqual(menu.price, 20)
        self.assertEqual(menu.description, 'A selection of Lunch items')

        # check that the calculate_total_cost method works correctly
        self.assertEqual(menu.calculate_total_cost(), 30)