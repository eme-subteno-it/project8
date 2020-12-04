import requests


class ApiFood:
    """
        Method for get the datas in the API OpenFoodFacts
    """

    def __init__(self):
        self.categories = []
        self.products = []

    def call_api(self, url, params=None):
        """ Method to call api by a request GET and return a json result """
        res = requests.get(url, params)
        result_parse = res.json()

        return result_parse

    def get_categories(self):
        """ Method for get 1000 categories """
        url = 'https://fr.openfoodfacts.org/categories.json'
        result_parse = self.call_api(url)

        for i in range(150):
            response_api = {}
            response_api['name'] = result_parse['tags'][i]['name']
            response_api['url'] = result_parse['tags'][i]['url'] + '.json'
            response_api['id'] = result_parse['tags'][i]['id']
            self.categories.append(response_api)

        return self.categories

    def get_products(self, categories):
        """ Method for get 20 products per pages in 1000 categories """

        url = 'https://fr.openfoodfacts.org/cgi/search.pl'

        for category in categories:
            params = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category.api_id,
                'page_size': 20,
                'json': 1,
            }
            result_parse = self.call_api(url, params)
            products = result_parse['products']

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

                            response_api['fat_level'] = product['nutrient_levels']['fat']
                            response_api['satured_fat_level'] = product['nutrient_levels']['saturated-fat']
                            response_api['sugars_level'] = product['nutrient_levels']['sugars']
                            response_api['salt_level'] = product['nutrient_levels']['salt']
                            response_api['fat_g'] = product['nutriments']['fat_100g']
                            response_api['satured_fat_g'] = product['nutriments']['saturated-fat_100g']
                            response_api['sugars_g'] = product['nutriments']['sugars_100g']
                            response_api['salt_g'] = product['nutriments']['salt_100g']

                            if product['product_name'] != '':
                                self.products.append(response_api)
                        except KeyError:
                            pass

        return self.products
