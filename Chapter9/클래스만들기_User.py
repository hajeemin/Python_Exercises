class User:
    def __init__(self, first_name, last_name, age, nationality, gender): # 속성(정보)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.gender = gender


    def describe_User(self): # 메서드(기능)
        print(f"User name : {self.first_name.title()} {self.last_name.upper()}")
        print(f"Age : {self.age}")
        print(f"Nationality : {self.nationality.title()}")
        print(f"Gender : {self.gender}")


    def greet(self): # 메서드(기능)
        print(f"\nHello, {self.first_name}! \nGood to see you!\n")

# User_A = User('jeemin', "ha",'34','Korean','F') # 객체1 (인스턴스)
# User_A.describe_User()
# User_A.greet()

# User_B = User('hyunseung','lee','34','Korean','M') # 객체2 (인스턴스)
# User_B.describe_User()
# User_B.greet()

class Admin(User):
    def __init__(self, first_name, last_name, age, nationality, gender):
        super().__init__(first_name, last_name, age, nationality, gender)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivilleges:")
        for privillege in self.privileges:
            print(f"-{privillege}")

jimin = Admin('jimin', 'ha', '34', 'korean','F')
jimin.describe_User()
jimin.privileges = [
    'can delet post',
    'cad add post',
    'can ban user'
]
jimin.show_privileges()