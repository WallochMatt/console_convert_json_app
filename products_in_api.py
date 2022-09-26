


class Product:
    def __init__(self, title, description, price, inventory_quantitiy, image_link):
        self.title = title
        self.description = description
        self.price = price
        self.inventory_quantity = inventory_quantitiy
        self.image_link = image_link




# @staticmethod
# def product_decoder(product):
#     return Product(product['title'], product['description'], product['price'], product['inventory_quantitiy'], product['image_link'])