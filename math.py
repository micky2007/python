def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x/y

def average(x, y):
    sum = add(x,y)
    return sum/2

def max(x,y):
    if x > y:
        return x
    if y > x:
        return y

def min(x,y):
    if x < y:
        return x
    if y < x:
        return y

while True:
    choice = input ("enter choice 1/2/3/4/5/6/7:")
    print (choice)

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2) )

        if choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2)  )

        if choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2) )

        if choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))

        if choice == '5':
            print("average of", num1, num2, '=', average(num1, num2) )

        if choice == '6':
            print("max number is", num1, '>', num2, '=', max(num1, num2) )

        if choice == '7':
            print("min number is", num1, '<', num2, '=', min(num1, num2) )



    else:
        print("invalid input")