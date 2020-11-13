import requests
from product.models import Category


class ApiFood:
    """
        Method for get the datas in the API OpenFoodFacts
    """

    def __init__(self):
        self.url = ''
        self.categories = []
        self.products = []
        self.result_parse = False

    def call_api(self, params=None):
        """ Method to call api by a request GET and return a json result """
        res = requests.get(self.url, params)
        self.result_parse = res.json()

    def get_categories(self):
        """ Method for get 1000 categories """
        self.url = 'https://fr.openfoodfacts.org/categories.json'
        self.call_api()

        for i in range(150):
            response_api = {}
            response_api['name'] = self.result_parse['tags'][i]['name']
            response_api['url'] = self.result_parse['tags'][i]['url'] + '.json'
            response_api['id'] = self.result_parse['tags'][i]['id']
            self.categories.append(response_api)

        return self.categories

    def get_products(self):
        """ Method for get 20 products per pages in 1000 categories """
        categories = Category.objects.all()
        self.url = 'https://fr.openfoodfacts.org/cgi/search.pl'

        for category in categories:
            params = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category.api_id,
                'page_size': 20,
                'json': 1,
            }
            self.call_api(params)
            products = self.result_parse['products']

            for product in products:
                if product:
                    if 'product_name' in product:
                        try:
                            response_api = {}
                            response_api['name'] = product['product_name']
                            response_api['desc'] = product['ingredients_text']
                            response_api['store'] = product['stores']
                            response_api['nutriscore'] = product['nutriscore_score']
                            response_api['nutriscore_grade'] = product['nutriscore_grade']
                            response_api['image'] = product['image_url']
                            response_api['url_api'] = product['url']
                            response_api['category_ids'] = product['categories_tags']
                            if product['product_name'] != '':
                                self.products.append(response_api)
                        except KeyError:
                            pass

        return self.products
