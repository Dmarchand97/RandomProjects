#########################################
#Ask user for 2 numbers, and with those 2 numbers find every common divisor they share
# (excluding the numbers themselves and 1)
#Give me number 1: 45
#Give me number 2: 60
#Common divisors: [3, 4, 5, 15]

def getnumber(one):
    return int(input(one))

def divisors():
    num1 = getnumber("Enter the first number: ")
    num2 = getnumber("Enter the second number: ")
    list1 = list(range(1, num1 + 1))
    list4 = list(range(1, num2 + 1))
    list2 = []
    list3 = []

    for x in list1:
        if x == 1:
            continue
        if num1 % x == 0:
            list2.append(x)
    for x in list4:
        if x == 1:
            continue
        if num2 % x == 0:
            list3.append(x)
    print(list2)
    print(list3)
    compare = set(list2) & set(list3)
    print(compare, "are the duplicate number(s), Hudson")

divisors()

