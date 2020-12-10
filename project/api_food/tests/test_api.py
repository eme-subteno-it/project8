from django.test import TestCase
from api_food.api import ApiFood
from product.models import Category


class ApiFoodTest(TestCase):

    def setUp(self):
        self.maxDiff = None
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
        self.product_mock = [
            {
                'name': 'Gazpacho',
                'desc': "Tomate, poivron, concombre, oignon, huile d'olive vierge extra (2,6%), vinaigre de vin, sel, ail et jus de citron. \r\n\r\nTeneur en légumes: 93%.",
                'store': 'Franprix,Magasins U,Auchan',
                'nutriscore': -4,
                'nutriscore_grade': 'a',
                'image': 'https://static.openfoodfacts.org/images/products/541/018/803/1072/front_fr.120.400.jpg',
                'url_api': 'https://fr.openfoodfacts.org/produit/5410188031072/gazpacho-alvalle',
                'category_ids': [
                    'en:plant-based-foods-and-beverages',
                    'en:beverages',
                    'en:plant-based-foods',
                    'en:fruits-and-vegetables-based-foods',
                    'en:meals', 'en:vegetables-based-foods',
                    'en:fresh-foods',
                    'en:soups',
                    'en:fresh-meals',
                    'en:refrigerated-foods',
                    'en:vegetable-soups',
                    'en:cold-soups',
                    'en:refrigerated-meals',
                    'en:gazpacho',
                    'en:refrigerated-soups'
                ],
                'fat_level': 'moderate',
                'satured_fat_level': 'low',
                'sugars_level': 'moderate',
                'salt_level': 'moderate',
                'fat_g': str(2.6),
                'satured_fat_g': str(0.4),
                'sugars_g': str(3.1),
                'salt_g': str(0.61)
            }
        ]

    def test_get_categories(self):
        result = []
        result_api = self.api.get_categories()
        result.append(result_api[0])
        result.append(result_api[1])
        self.assertEqual(result, self.categories_mock)

    def test_get_products(self):
        result = []
        result_api = self.api.get_products(self.categories)
        result.append(result_api[0])
        self.assertEqual(result, self.product_mock)
