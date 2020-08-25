""""This module is an attempt to practice class in python.""""""


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.dog_name = name
        self.dog_age = age
        self.name = "Rambo"
        self.age = 12

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.dog_name} is now sitting")

    def roll_over(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.dog_age} rolled over!")


my_dog = Dog("Maxwell", 6)
