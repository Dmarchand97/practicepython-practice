#write a program that returns a list that contains only the elements that are common between the lists

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list3 = []

for i in list1:
    if i in list2:
      list3.append(i)

print(list3)