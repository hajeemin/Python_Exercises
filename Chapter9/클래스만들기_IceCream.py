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
        self.reorders = []
        

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

    def show_sold_outs(self, flavors):
        for flavor in flavors:
            self.soldouts.append(flavor)
            self.flavors.remove(flavor)
        print(f"\nCurrently Sold Out:")
        for soldout in self.soldouts:
            print(f"-{soldout}")

    def show_reorders(self, flavors):
        self.reorders.extend(flavors)
        print(f"\nReorder list:")
        for flavor in self.reorders:
            print(f"-{flavor}")

    def show_restocks(self, flavors):
        for flavor in flavors:
            if flavor in self.flavors:
                pass
            else:
                self.flavors.append(flavor)
            self.soldouts.remove(flavor)

            print(f"\n{flavor} is now restocked!")


    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"\nYes, We have {flavor} now! ")
        else:
            print(f"\nSorry, we don't have {flavor} right now..")

    def calculate_price(self):
        number = int(input("\nNumber of ice-cream you'd like to order:"))
        price = number * 5000
        return price

    def closing(self):
        print(f"{self.name} is closed.")
        

big_one = IceCreamStand('The Big one')
big_one.flavors = ['vanila', 'chocolate', 'black cherry', 'mint','pistachio', 'strawberry']

big_one.show_sold_outs(['vanila'])
# big_one.show_flavors()
big_one.check_flavor('vanila')
big_one.show_restocks(['vanila'])