# tests/test-views.py
from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(
            title="Burger", price=10.99, inventory=50)
        self.menu2 = Menu.objects.create(
            title="Pizza", price=15.99, inventory=30)
        # Add more menu items as needed

    def test_getall(self):
        response = self.client.get("/restaurant/menu/items")
        self.assertEqual(response.status_code, 200)

        menu_data = response.data
        # Check if the response contains all added menu items
        self.assertEqual(len(menu_data), 4)

