#Divisors
#Create a program that asks the user for a number and then prints out a list of all the divisors

num = int(input("Please enter a number: "))

list1 = list(range(1, num+1))
list2 = []

for x in list1:
    if x == 1:
        continue
    if num % x == 0:
        list2.append(x)


print(list2)
