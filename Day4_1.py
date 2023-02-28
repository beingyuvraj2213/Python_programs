# randint(a,b) -> returns a random integer between a & b
# random() -> returns floating no between 0 and 1
# random is a module  
import random
import my_module
random_integer = random.randint(1,5)
# print(random_integer)
# print(my_module.Pi)
random_float=random.random()
# print(random_float)
num=random_integer+random_float
print(num)
