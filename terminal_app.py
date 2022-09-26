
from urllib import response
import json
from types import SimpleNamespace
import requests

from products_in_api import Product

class App:
    def __init__(self):
        pass

    @staticmethod
    def get_all_products():
        try:
            response = requests.get(f'http://127.0.0.1:8000/api/products/')
            products = response.json()
            print("All products:")
            for product in products:
                print(f" ID: {product['id']} - {product['title']}")
        except:
            print("Something went wrong")
    
    
    @staticmethod
    def post_product():
        product = {
            'title': str(input("Product title: ")), 
            'description' : str(input("Description: ")),
            'price': float(input('Price: ')),
            'inventory_quantity': int(input('In stock: ')),
        }

        try:
            temp = int(input("Do you have an image link? If yes, enter: 1"))
            if temp == 1:
                product['image_link'] = str(input('Enter link'))
        except:
            pass
    

        response = requests.post('http://127.0.0.1:8000/api/products/', json = product)
        print(response.content)
        new_product = response.json()
        
        print(f"""
Title: {new_product['title']}
Description: {new_product['description']}
Price: ${new_product['price']}
In Stock: {new_product['inventory_quantity']}
Image Link: {new_product['image_link']}""")


    @staticmethod
    def get_product(id):
        try:
            response = requests.get(f'http://127.0.0.1:8000/api/products/{str(id)}/')
            product = response.json()
            print(f"""Title: {product['title']}
Description: {product['description']}
Price: ${product['price']}
In Stock: {product['inventory_quantity']}
Image Link: {product['image_link']}""")
        
        except:
            print("Something went wrong")


    @staticmethod
    def put_product(id):
        product = {
            'title': str(input("Product title: ")), 
            'description' : str(input("Description: ")),
            'price': float(input('Price: ')),
            'inventory_quantity': int(input('In stock: ')),
        }
        try:
            temp = int(input("Do you have an image link? If yes, enter: 1"))
            if temp == 1:
                product['image_link'] = str(input('Enter link'))
        except:
            pass
    

        response = requests.put(f'http://127.0.0.1:8000/api/products/{str(id)}/', json=product)
        updated_product = response.json()


    @staticmethod
    def delete_product(id):
        try:
            requests.delete(f'http://127.0.0.1:8000/api/products/{str(id)}/')
        except:
            print('Error')