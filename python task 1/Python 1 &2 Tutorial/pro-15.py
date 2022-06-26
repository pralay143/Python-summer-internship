list = []

n = int(input("Enter the number of elements : "))

# Range function
for i in range(0,n):
    Element = input('Enter the elements : ')

    list.append(Element)

tuple = tuple(list)
print(list)
print(tuple)

