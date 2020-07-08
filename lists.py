print("Micky is awesome")
print("learning python lists")


fruitlist = ["apple", "bannana", "cherry", "strawberry"]
print(fruitlist)

for fruit in fruitlist:
    print("fruit")

numberlist = [100, 200, 300, 4000, 1000]
print(numberlist)
total = 0
for number in numberlist:
    print(number)
    total = total + number

print(total)

newlist = [4, 5, 6, 7, 8]
print(newlist)

sum = 0
average = 0
count = 0

for number in newlist:
    sum = sum + number
    if(count == 0):
        min = number
    elif (number < min):
        min = number
    count = count + 1


print(sum)
average = sum/len(newlist)
print(average)
print(min)


