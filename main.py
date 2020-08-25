import json
class Dog:

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.dog_name = name
        self.dog_age = age
        self.name = "Rambo"
        self.age = 12

    def sit(self):
        print(f"{self.dog_name} is now sitting")

    def roll_over(self):
        print(f"{self.dog_age} rolled over!")

my_dog = Dog("Maxwell", 6)