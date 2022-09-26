
from urllib import response
import json
from types import SimpleNamespace
import requests

from products_in_api import Product


#Like battlefield, holds the request methods
class App:
    def __init__(self):
        self.temp = Product

    def get_product(id):
        response = requests.get(f'http://127.0.0.1:8000/api/products/{str(id)}/')
        print(response.content)
        print('\n')
        product = response.json()
        print(f"""Title: {product['title']}
Description: {product['description']}
Price: ${product['price']}
In Stock: {product['inventory_quantity']}
Image Link: {product['image_link']}""")