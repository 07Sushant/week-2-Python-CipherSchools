# numbers  = list(range(1,11))
# print(numbers)

# print(numbers.pop(2))
# # print(numbers)
# print(numbers.index(1,2))

numbers = [1,2,3,4,5,6,7,8,9,10]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))