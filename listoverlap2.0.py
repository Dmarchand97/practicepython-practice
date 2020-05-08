#list overlap
#program that returns a list that contains only the elements that are common between the lists
import random
randomList1 = [random.randint(0, 20) for i in range(10)]
randomList2 = [random.randint(0, 20) for i in range(10)]
print(randomList1)
print(randomList2)

c = []

for i in randomList1 and randomList2:
    c.append(i)

print(c)
