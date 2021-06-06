input1 = input("Enter the sequence of lines:")
lst = []
for i in input1.split(' '):
    lst.append(i.upper())

print(' '.join(lst))