""" All tests for the api_food api.py application """
from django.test import TestCase
from api_food.api import ApiFood
from product.models import Category


class ApiFoodTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Aliments et boissons à base de végétaux',
            url_product='https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux.json',
            api_id='en:plant-based-foods-and-beverages'
        )
        self.category2 = Category.objects.create(
            name="Aliments d'origine végétale",
            url_product='https://fr.openfoodfacts.org/categorie/aliments-d-origine-vegetale.json',
            api_id='en:plant-based-foods'
        )
        self.categories = []
        self.categories.append(self.category)
        self.categories.append(self.category2)
        self.api = ApiFood()
        self.categories_mock = [
            {
                'name': 'Aliments et boissons à base de végétaux',
                'url': 'https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux.json',
                'id': 'en:plant-based-foods-and-beverages'
            },
            {
                'name': "Aliments d'origine végétale",
                'url': 'https://fr.openfoodfacts.org/categorie/aliments-d-origine-vegetale.json',
                'id': 'en:plant-based-foods'
            }
        ]

    def test_get_categories(self):
        result = []
        result_api = self.api.get_categories()
        result.append(result_api[0])
        result.append(result_api[1])
        self.assertEqual(result, self.categories_mock)
