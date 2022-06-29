# Example of "NON KEYWORD NONARGUMENT"
def sum(*num):
    sum = 0

    for n in num:
        sum = sum + n
    print("Sum is : ",sum)

sum(50,100)
sum(110,111,222)
sum(99,88,77,66)
