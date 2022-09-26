#utilizes this API https://github.com/WallochMatt/products_backend_api
from terminal_app import App

#i could set up the ui here or eslewhere to ask what the user wants and send it with inputs where it needs to go
run = App


user_response = int(input("""
How would you like to access the database?
Find all products: 1
Find a particular product: 2
Update a product: 3
Create a product: 4
Delete a product: 5
"""))

if user_response == 1:
    run.get_all_products() #ALL
elif user_response == 2:
    run.get_product(int(input('Insert product ID to find')))
elif user_response == 3:
    run.put_product(int(input('Insert product ID to update')))
elif user_response == 4:
    run.post_product()#CREATE
elif user_response == 5:
    run.delete_product(int(input('Insert product ID to delete')))