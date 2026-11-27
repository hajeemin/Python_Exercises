# 아이스크림 가판대를 레스토랑 클래스 상속하여 만들어보기

class Restaurant:

    def __init__(self, name, cuisine_type): # 속성(정보)
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self): # 메서드(기능)_1
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type.title()}")
    
    def open_restuarant(self): # 메서드(기능)_2
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        self.number_served = number
        print(f"We served {self.number_served} customers today.")

    def increment_number_served(self, number):
        self.number_served += number
        print(f" {number} more customers visited.")
        print(f"There were {self.number_served} customers in total today. ")

################################################################################

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type = 'ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []
        self.soldouts = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

    def show_sold_outs(self, flavor):
        self.soldouts.append(flavor)
        print(f"\n Currently Sold Out:")
        for soldout in self.soldouts:
            print(f"-{soldout.title()}")
        self.flavors.remove(flavor)

big_one = IceCreamStand('The Big one')
big_one.flavors = ['vanila', 'chocolate', 'black cherry']
big_one.describe_restaurant()
big_one.show_sold_outs('vanila')
big_one.flavors.append('strawberry')
big_one.show_flavors()
big_one.set_number_served(40)

