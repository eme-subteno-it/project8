from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    store = models.CharField(max_length=200)
    nutriscore = models.IntegerField()
    nutriscore_grade = models.CharField(max_length=2)
    image = models.URLField()
    url_api = models.URLField()
    category_ids = models.ManyToManyField('Category', related_name='+')

    @classmethod
    def create_product(cls, name, description, store, nutriscore, nutriscore_grade, image, url_api, category_ids):
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
        )
        for categ in categ_ids:
            product.category_ids.add(categ)

        return product


class Category(models.Model):
    name = models.CharField(max_length=200)
    url_product = models.URLField()
    api_id = models.CharField(max_length=200)
