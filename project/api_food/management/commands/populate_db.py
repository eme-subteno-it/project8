""" Inherit class to customize an command """
from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from api_food.api import ApiFood
from product.models import Category, Product


class Command(BaseCommand):
    """ Customize command to populate the database products and categories """

    help = _('Populating the database via the Openfoodfact API')
    api_food = ApiFood()

    def add_arguments(self, parser):
        """ Add argument to the command to delete products and categories """
        parser.add_argument(
            '--delete',
            action='store_true',
            help=_('Delete products and categories instead of closing it'),
        )

    def handle(self, *args, **options):
        """
            Manage the command for :
            - delete the products and categories in database
            - populate the database with categories and products
        """
        # If arg --delete
        if options['delete']:
            categories = Category.objects.all()
            products = Product.objects.all()
            if products:
                Product.objects.all().delete()
            if categories:
                Category.objects.all().delete()
                self.stdout.write(_('The products and their categories have been deleted'))
            else:
                self.stdout.write(_('The database is already empty.'))
        else:
            # Management categories
            self.stdout.write(_('Add the categories from api OpenfoodFact'))
            new_categories = self.api_food.get_categories()

            for categ in new_categories:
                category = Category.objects.filter(name=categ['name'])
                if not category.exists():
                    category = Category.objects.create(
                        name=categ['name'],
                        url_product=categ['url'],
                        api_id=categ['id']
                    )

            # Management products
            self.stdout.write(_('Add the products now'))
            new_products = self.api_food.get_products(Category.objects.all())

            for prod in new_products:
                product = Product.objects.filter(name=prod['name'])
                if not product.exists():
                    product = Product()
                    Product.create_product(
                        name=prod['name'],
                        description=prod['desc'],
                        store=prod['store'],
                        nutriscore=prod['nutriscore'],
                        nutriscore_grade=prod['nutriscore_grade'],
                        image=prod['image'],
                        url_api=prod['url_api'],
                        category_ids=prod['category_ids'],
                        fat_level=prod['fat_level'],
                        satured_fat_level=prod['satured_fat_level'],
                        sugars_level=prod['sugars_level'],
                        salt_level=prod['salt_level'],
                        fat_g=prod['fat_g'],
                        satured_fat_g=prod['satured_fat_g'],
                        sugars_g=prod['sugars_g'],
                        salt_g=prod['salt_g']
                    )
