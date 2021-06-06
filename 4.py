n = input("Enter words with - sperated:")
s= []
for i in n.split('-'):
    s.append(i)
s.sort()   
print('-'.join(s))