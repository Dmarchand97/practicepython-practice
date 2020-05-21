###############################################
#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order.

def reverseword():
    word = input("Please enter multiple words: ")
    #input the string to split
    result = word.split()
    #split each word not includeing any whitespaces
    #print(result)
    a = result[0:][::-1]
    #reverses the string
    reverse = " ".join(a)
    #enters back the whitespaces
    print(word)
    #print original
    print(reverse)
    #print the reverse


reverseword()
#display funtion