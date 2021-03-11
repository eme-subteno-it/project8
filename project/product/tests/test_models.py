""" All tests for the product models application """
from django.test import TestCase
from product.models import Product, Category
from user.models import User


class ProductModelTest(TestCase):
    """
        Testing the Product model.
        This class create a product in database test,
        a user, a category and 2 substitutes to test
        if a user can saved or delete a substitute,
        calculate a substitute and if the attributes
        are well defined.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )
        self.category = Category.objects.create(
            name='Boisson',
        )
        self.product = Product.objects.create(
            name='Jus d\'orange',
            description='description',
            store='Auchan',
            nutriscore='3',
            nutriscore_grade='c',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
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
        self.substitute = Product.objects.create(
            name='Jus d\'abricot',
            description='description',
            store='Auchan',
            nutriscore='1',
            nutriscore_grade='a',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )
        self.substitute2 = Product.objects.create(
            name='Jus de banane',
            description='description',
            store='Auchan',
            nutriscore='2',
            nutriscore_grade='b',
            image='https://static.openfoodfacts.org/images/products/322/885/700/0852/front_fr.134.400.jpg',
            url_api='https://fr.openfoodfacts.org/produit/3502110009449/pur-jus-d-orange-sans-pulpe-tropicana',
            fat_level='low',
            satured_fat_level='low',
            sugars_level='moderate',
            salt_level='low',
            fat_g=0,
            satured_fat_g=0,
            sugars_g=8.9,
            salt_g=0
        )
        self.substitute.category_ids.add(self.category)
        self.substitute2.category_ids.add(self.category)

    def test_name_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_store_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('store').max_length
        self.assertEqual(max_length, 200)

    def test_nutriscore_grade_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('nutriscore_grade').max_length
        self.assertEqual(max_length, 2)

    def test_fat_level_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('fat_level').max_length
        self.assertEqual(max_length, 15)

    def test_satured_fat_level_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('satured_fat_level').max_length
        self.assertEqual(max_length, 15)

    def test_sugars_level_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('sugars_level').max_length
        self.assertEqual(max_length, 15)

    def test_salt_level_max_length(self):
        product = Product.objects.get(id=self.product.id)
        max_length = product._meta.get_field('salt_level').max_length
        self.assertEqual(max_length, 15)

    def test_calculate_substitutes(self):
        product = Product.objects.get(id=self.product.id)
        self.assertCountEqual(product.calculate_substitutes(20), [self.substitute, self.substitute2])

    def test_save_substitute(self):
        product = Product.objects.get(id=self.product.id)
        self.assertTrue(product.save_substitute(self.user))

    def test_delete_substitute(self):
        product = Product.objects.get(id=self.product.id)
        self.assertTrue(product.delete_substitute(self.user))


class CategoryModelTest(TestCase):
    """
        Testing the Category model.
        This class create a category in database test,
        to test if the attributes are well defined.
    """
    def setUp(self):

        self.category = Category.objects.create(
            name='Boisson',
            api_id='en:dried-products-to-be-rehydrated',
        )

    def test_name_max_length(self):
        category = Category.objects.get(id=self.category.id)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_api_id_max_length(self):
        category = Category.objects.get(id=self.category.id)
        max_length = category._meta.get_field('api_id').max_length
        self.assertEqual(max_length, 200)
