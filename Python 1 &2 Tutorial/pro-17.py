dict = {}
n = int(input("Enter the value of element : "))

for i in range(0,n):
    a,b = input("Enter key value pair data : ").split()
    dict[a] = [b]
    print(dict)
