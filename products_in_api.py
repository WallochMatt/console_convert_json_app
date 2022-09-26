


class Product:
    def __init__(self):
        pass





@staticmethod
def product_decoder(product):
    return Product(product['title', 'description', 'price', 'inventory_quantitiy', 'image_link'])