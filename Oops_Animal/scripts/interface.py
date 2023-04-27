# interfaces.py

from abc import ABC, abstractmethod

class PetInterface(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def feed(self, food):
        pass