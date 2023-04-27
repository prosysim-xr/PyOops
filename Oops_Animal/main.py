# main.py

# Importing classes from other files
from scripts.animal import Animal
from scripts.dog import Dog
from scripts.cat import Cat

# Creating objects
dog = Dog('Buddy', 'Golden Retriever', 'Woof')
cat = Cat('Mittens', 'Gray', 'Meow')

# Calling methods
dog.make_sound()  # Output: Buddy says Woof
cat.scratch()     # Output: Mittens is scratching


# main.py // other way

# Importing classes from other files
from scripts.cat import Cat
from scripts.dog import Dog

# Creating objects
dog = Dog('Buddy', 'Golden Retriever', 'Woof')
cat = Cat('Mittens', 'Gray', 'Meow')

# Calling methods
dog.make_sound()  # Output: Buddy says Woof
cat.scratch()     # Output: Mittens is scratching
dog.play()        # Output: Buddy is playing
cat.play()        # Output: Mittens is playing
dog.feed('kibble') # Output: Buddy is eating kibble
cat.feed('tuna')   # Output: Mittens is eating tuna

