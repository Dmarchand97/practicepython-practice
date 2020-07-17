# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
import random

def elementSearch():
    #create a list of 10 numbers ranging from 0-30
    randomList = [random.randint(0, 30) for i in range(10)]
    print(randomList)
    #sort the list from least to greatest
    randomList.sort()
    #random number
    randomNum = random.randint(1, 50)
    print(randomNum)
    #check if random number is in the list
    if randomNum in randomList:
        print("True")

    else:
        print("False")



elementSearch()