#String Lists
#Ask the user for a string and print out whether this string is a palindrome or not

string1 = input("Please enter a word: ")
a = string1[0:][::-1]
for i in string1:
    if a == string1:
        print("Its a palindrome")
    else:
        print("wrong")
    break


