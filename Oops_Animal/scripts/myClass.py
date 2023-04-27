# overloading
class MyClass:
    def my_method(self, a, b=None, c=None):
        if b is None and c is None:
            print(f"a = {a}")
        elif c is None:
            print(f"a + b = {a + b}")
        else:
            print(f"a + b + c = {a + b + c}")

obj = MyClass()

obj.my_method(1)          # Output: a = 1
obj.my_method(1, 2)       # Output: a + b = 3
obj.my_method(1, 2, 3)    # Output: a + b + c = 6

# over riding is in inheritance.