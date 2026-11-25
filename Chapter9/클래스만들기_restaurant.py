class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type.title()}")
    
    def open_restuarant(self):
        print(f"{self.name} is now open!")

my_restaurant = Restaurant('Kiwajip','Korean')

print(f"The name of the restaurant is {my_restaurant.name.upper()}.")
print(f"Cuisine type of {my_restaurant.name.upper()} is {my_restaurant.cuisine_type.title()}.")

my_restaurant.open_restuarant()
