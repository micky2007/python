def convertCtoF(celcius):
    farenheight = celcius * 1.8 + 32
    return farenheight

celcius = 30
farenheight = celcius * 1.8 + 32

while True:
    choice = input ("enter c/f: ")
    print (choice)

    if choice in ('c', 'f'):


        num1 = float(input("enter number: "))
        if choice == 'c':
            print(convertCtoF(num1))