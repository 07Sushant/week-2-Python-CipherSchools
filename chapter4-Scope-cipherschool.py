# scope
x = 5 #global variable

def func():
    global x
    x = 7  #local variable jo function ke andr define ho wahi tak scope
    return x

print(x)
print(func())
print(x)