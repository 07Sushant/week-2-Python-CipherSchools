def func(int1, int2):
    add = int1+int2
    multiply = int1*int2
    return add, multiply
# print(func(2,3))  # this if return function two value then tuples comes

add, multiply = func(2,3)
print(add, multiply)