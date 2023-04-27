from lib.calculator import Calculator
from myFolder.other_calculator import Calculator

c = Calculator()

result = c.add(2, 3)
print(result)

result = c.subtract(5, 2)
print(result)

result = c.multiply(3, 4)
print(result)

result = c.divide(10, 2)
print(result)