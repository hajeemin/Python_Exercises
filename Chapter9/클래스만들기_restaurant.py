# class Restaurant:

#     def __init__(self, name, cuisine_type): # 속성(정보)
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self): # 메서드(기능)_1
#         print(f"Restaurant name: {self.name}")
#         print(f"Cuisine type: {self.cuisine_type.title()}")
    
#     def open_restuarant(self): # 메서드(기능)_2
#         print(f"{self.name} is now open!")

# restaurant_A = Restaurant('Kiwajip','Korean') #인스턴스 A (객체)

# # print(f"The name of the restaurant is {my_restaurant.name.upper()}.")
# # print(f"Cuisine type of {my_restaurant.name.upper()} is {my_restaurant.cuisine_type.title()}.")

# restaurant_A.describe_restaurant() # 메서드
# restaurant_A.open_restuarant() # 메서드

# restaurant_B = Restaurant('Casamia', 'Italian') #인스턴스 B (객체)

# restaurant_B.describe_restaurant() # 메서드
# restaurant_B.open_restuarant() # 메서드

# restaurant_C = Restaurant('Chunsang','Chinese') #인스턴스 C (객체)
# restaurant_C.describe_restaurant() # 메서드
# restaurant_C.open_restuarant() # 메서드



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
        print(f"We served {self.number_served} customers today.")\

    def increment_number_served(self, number):
        self.number_served += number
        print(f" {number} more customers visited.")
        print(f"There were {self.number_served} customers in total today. ")

restaurant= Restaurant('Kiwajip','Korean') #인스턴스 A (객체)

restaurant.set_number_served(50)
restaurant.increment_number_served(2)

