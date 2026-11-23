class Dog:
    #개를 표현해보기
    
    def __init__(self, name, age):
        # name과 age 속성 초기화
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def hands(self):
        print(f"{self.name} is handing a paw.")

    


my_dog = Dog('chopa', 7)

# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age}years old.")

my_dog.sit()
my_dog.roll_over()


your_dog = Dog('thunder', 2)

your_dog.sit()


