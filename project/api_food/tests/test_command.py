""" Inherit class to customize a command """
from io import StringIO
from django.test import TestCase, override_settings
from django.core.management import call_command
from product.models import Product, Category


class CommandTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Boisson',
            api_id='en:dried-products-to-be-rehydrated'
        )
        self.product = Product.objects.create(
            name='Jus d\'abricot',
            description='description',
            store='Auchan',
            nutriscore='1',
            nutriscore_grade='a',
            image='https://static.openfoodfacts.org/images/products/322/885/\
                700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-\
                jus-d-orange-sans-pulpe-tropicana',
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )
        self.product.category_ids.add(self.category)

    @classmethod
    def call_command(cls, *args, **kwargs):
        out = StringIO()
        call_command(
            "populate_db",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_delete_db(self):
        out = self.call_command('--delete')
        self.assertEqual(out, 'The products and their categories have been deleted\n')

    @override_settings(LANGUAGE_CODE='en-US', LANGUAGES=(('en', 'English'),))
    def test_delete_db_without_products(self):
        # Delete the database before for the test
        Product.objects.all().delete()
        Category.objects.all().delete()

        out = self.call_command('--delete')
        self.assertEqual(out, 'The database is already empty.\n')
