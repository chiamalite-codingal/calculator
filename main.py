a = int(input("Enter a:"))
b = int(input("Enter b:"))
print("select options:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

option = input("Enter a or b or c or d:")

def add(a,b):
    return a+b
print(add(a,b))

def sub(a,b):
    return a-b
print(sub(a,b))

def mul(a,b):
    return a*b
print(mul(a,b))

def div(a,b):
    return a/b
print(div(a,b))

if option =="a":
    print(add(a,b))
elif option == "b":
    print(sub(a,b))
elif option == "c":
    print(mul(a,b))
elif option == "d":
    print(div(a,b))