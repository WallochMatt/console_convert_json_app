#utilizes this API https://github.com/WallochMatt/products_backend_api
from terminal_app import App


using_app = True
while using_app == True:

    user_response = int(input("""
How would you like to access the database?
Find all products: 1
Find a particular product: 2
Update a product: 3
Create a product: 4
Delete a product: 5
Exit the app: 9
"""))

    if user_response == 1:
        App.get_all_products() #ALL
    elif user_response == 2:
        App.get_product(int(input('Insert product ID to find')))
    elif user_response == 3:
        App.put_product(int(input('Insert product ID to update')))
    elif user_response == 4:
        App.post_product()#CREATE
    elif user_response == 5:
        App.delete_product(int(input('Insert product ID to delete')))
    elif user_response == 9:
        using_app = False

    input("Enter to continue")