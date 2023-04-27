# Example of OOPs in Python

# 1. Class creation
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    # 2. Encapsulation
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
    
    # 5. Polymorphism
    def feed(self, food):
        print(f"{self.name} is eating {food}")
        
# 4. Inheritance
class Dog(Animal):
    def __init__(self, name, breed, sound):
        super().__init__(name, 'Dog', sound)
        self.breed = breed
        
    def fetch(self):
        print(f"{self.name} is fetching")

# 3. Modularity
class Cat(Animal):
    def __init__(self, name, color, sound):
        super().__init__(name, 'Cat', sound)
        self.color = color
        
    def scratch(self):
        print(f"{self.name} is scratching")
        

# Creating objects
dog = Dog('Buddy', 'Golden Retriever', 'Woof')
cat = Cat('Mittens', 'Gray', 'Meow')

# Accessing attributes
print(dog.name)   # Output: Buddy
print(cat.color)  # Output: Gray

# Calling methods
dog.make_sound()  # Output: Buddy says Woof
cat.scratch()     # Output: Mittens is scratching

# Using polymorphism
dog.feed('bones')  # Output: Buddy is eating bones
cat.feed('fish')   # Output: Mittens is eating fish

# Using inheritance
dog.fetch()  # Output: Buddy is fetching
