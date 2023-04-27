# pet.py

from scripts.interfaces import PetInterface

class Pet(PetInterface):
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
        
    def play(self):
        print(f"{self.name} is playing")
        
    def feed(self, food):
        print(f"{self.name} is eating {food}")