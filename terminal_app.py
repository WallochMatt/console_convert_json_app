
from urllib import response
import json
from types import SimpleNamespace
import requests

from products_in_api import Product


#Like battlefield, holds the request methods
class App:
    def __init__(self):
        self.temp = Product



    def get_all_products():
        response = requests.get(f'http://127.0.0.1:8000/api/products/')
        products = response.json()
        print("All products:")
        for product in products:
            print(f"{product['title']} ID: {product['id']}")
    
    
    def get_product(id):
        response = requests.get(f'http://127.0.0.1:8000/api/products/{str(id)}/')
        # print(response.content)
        # print('\n')
        product = response.json()
        print(f"""Title: {product['title']}
Description: {product['description']}
Price: ${product['price']}
In Stock: {product['inventory_quantity']}
Image Link: {product['image_link']}""")


# @staticmethod
# def product_decoder(product):
#     return Product(product['title'], product['description'], product['price'], product['inventory_quantity'], product['image_link'])
