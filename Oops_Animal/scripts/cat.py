# cat.py

from scripts.animal import Animal

class Cat(Animal):
    def __init__(self, name, color, sound):
        super().__init__(name, 'Cat', sound)
        self.color = color
        
    def scratch(self):
        print(f"{self.name} is scratching")



# cat.py // next way type

from scripts.pet import Pet

class Cat(Pet):
    def __init__(self, name, color, sound):
        super().__init__(name, 'Cat', sound)
        self.color = color
        
    def scratch(self):
        print(f"{self.name} is scratching")
