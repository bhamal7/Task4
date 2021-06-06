n = int(input("Enter the number upto which you wanna find the values:"))
lst = []
for i in range(1,n+1):
    lst.append(i)
result = filter(lambda i: i % 7 == 0 and i % 3 != 0,lst)
print(list(result))