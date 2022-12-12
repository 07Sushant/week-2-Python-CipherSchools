# make a function jo ek list ke element ka suare retuen kre
def sqaure_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

numbers = list(range(1,11))
print(sqaure_list(numbers))