class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 자동차 속성(정보)
        self.odometer_reading = 0

    def get_descriptive_name(self): # 메소드 
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        # 자동차 메서드 (기능) : 자동차 정보들을 어떻게 조합하는지. 여기서 근데 왜 굳이 리턴을? 뭔가 더 간결하게 줄이고싶을때 리턴을 쓸 것 같은데 맞나

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        pass

# my_new_Car = Car('audi','a4', '2024')
# print(my_new_Car.get_descriptive_name())

# my_new_Car.odometer_reading = 23
# my_new_Car.read_odometer()

# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

##################자식 클래스 만들기######################
class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
