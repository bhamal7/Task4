
lst =[]
for i in range(1,21):
    lst.append(i)


evenlist = filter(lambda i: i %2 == 0, lst)
print(list(evenlist))