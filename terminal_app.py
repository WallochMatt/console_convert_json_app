
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
    

    def post_product():
        product = {
            'title': str(input("Product title: ")), 
            'description' : str(input("Description: ")),
            'price': float(input('Price: ')),
            'inventory_quantity': int(input('In stock: ')),
            'image_link': str(input("COPY IF NO IMAGE: https://as2.ftcdn.net/v2/jpg/00/89/55/15/1000_F_89551596_LdHAZRwz3i4EM4J0NHNHy2hEUYDfXc0j.jpg")),
        }

        response = requests.post('http://127.0.0.1:8000/api/products/', json = product)
        print(response.content)
        new_product = response.json()
        
        print(f"""
Title: {new_product['title']}
Description: {new_product['description']}
Price: ${new_product['price']}
In Stock: {new_product['inventory_quantity']}
Image Link: {new_product['image_link']}""")


    
    def get_product(id):
        response = requests.get(f'http://127.0.0.1:8000/api/products/{str(id)}/')
        product = response.json()
        print(f"""Title: {product['title']}
Description: {product['description']}
Price: ${product['price']}
In Stock: {product['inventory_quantity']}
Image Link: {product['image_link']}""")


    def put_product(id):
        product = {
            'title': str(input("Product title: ")), 
            'description' : str(input("Description: ")),
            'price': float(input('Price: ')),
            'inventory_quantity': int(input('In stock: ')),
            'image_link': str(input("COPY IF NO IMAGE: https://as2.ftcdn.net/v2/jpg/00/89/55/15/1000_F_89551596_LdHAZRwz3i4EM4J0NHNHy2hEUYDfXc0j.jpg")),
        }
        response = requests.put(f'http://127.0.0.1:8000/api/products/{str(id)}/', json=product)
        updated_product = response.json()







# @staticmethod
# def product_decoder(product):
#     return Product(product['title'], product['description'], product['price'], product['inventory_quantity'], product['image_link'])
