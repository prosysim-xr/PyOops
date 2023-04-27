# dog.py

from scripts.animal import Animal

class Dog(Animal):
    def __init__(self, name, breed, sound):
        super().__init__(name, 'Dog', sound)
        self.breed = breed
        
    def fetch(self):
        print(f"{self.name} is fetching")


# dog.py // interface type

from scripts.pet import Pet

class Dog(Pet):
    def __init__(self, name, breed, sound):
        super().__init__(name, 'Dog', sound)
        self.breed = breed
        
    def fetch(self):
        print(f"{self.name} is fetching")

