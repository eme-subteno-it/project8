import string
import random
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    store = models.CharField(max_length=200)
    nutriscore = models.IntegerField()
    nutriscore_grade = models.CharField(max_length=2)
    image = models.URLField()
    url_api = models.URLField()
    category_ids = models.ManyToManyField('Category')
    user_ids = models.ManyToManyField('user.User')

    fat_level = models.CharField(max_length=15, default=None)
    satured_fat_level = models.CharField(max_length=15, default=None)
    sugars_level = models.CharField(max_length=15, default=None)
    salt_level = models.CharField(max_length=15, default=None)

    fat_g = models.FloatField(default=0.0)
    satured_fat_g = models.FloatField(default=0.0)
    sugars_g = models.FloatField(default=0.0)
    salt_g = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        self.nutriscore_grade = self.nutriscore_grade.upper()
        return super(Product, self).save(*args, **kwargs)

    @classmethod
    def create_product(cls, name, description, store, nutriscore, nutriscore_grade, image, url_api, category_ids, fat_level, satured_fat_level, sugars_level, salt_level, fat_g, satured_fat_g, sugars_g, salt_g):
        categ_ids = []
        for category in category_ids:
            try:
                category_id = Category.objects.get(api_id=category)
                categ_ids.append(category_id.id)
            except Category.DoesNotExist:
                pass

        product = cls.objects.create(
            name=name,
            description=description,
            store=store,
            nutriscore=nutriscore,
            nutriscore_grade=nutriscore_grade,
            image=image,
            url_api=url_api,
            fat_level=fat_level,
            satured_fat_level=satured_fat_level,
            sugars_level=sugars_level,
            salt_level=salt_level,
            fat_g=fat_g,
            satured_fat_g=satured_fat_g,
            sugars_g=sugars_g,
            salt_g=salt_g,
        )
        for categ in categ_ids:
            product.category_ids.add(categ)

        return product

    def calculate_substitutes(self):
        all_substitutes = []

        nutriscore_grade = string.ascii_uppercase.index(self.nutriscore_grade)
        nutriscore = self.nutriscore

        category_ids = self.category_ids.all().values_list('id', flat=True)

        for categ in category_ids:
            products = Category.objects.get(id=categ).product_set.all()
            for product in products:
                if product.nutriscore < nutriscore:
                    nutriscore_grade_substitute = string.ascii_uppercase.index(product.nutriscore_grade)
                    if nutriscore_grade_substitute < nutriscore_grade:
                        if product not in all_substitutes:
                            all_substitutes.append(product)

        if len(all_substitutes) > 30:
            substitutes = random.sample(all_substitutes, 30)
        else:
            substitutes = random.sample(all_substitutes, len(all_substitutes))

        return substitutes

    def save_substitute(self, user):
        try:
            self.user_ids.add(user.id)
            return True
        except user.DoesNotExist:
            return False

    def delete_substitute(self, user):
        try:
            self.user_ids.remove(user.id)
            return True
        except user.DoesNotExist:
            return False


class Category(models.Model):
    name = models.CharField(max_length=200)
    url_product = models.URLField()
    api_id = models.CharField(max_length=200)
