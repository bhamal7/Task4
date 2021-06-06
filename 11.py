lst = [1,2,3,4,5,6,7,8,9,10]
lst2 = filter(lambda i: i % 2 == 0 , lst)
evenlist = list(lst2)
print(evenlist)
lst3 = map(lambda i: i**2,evenlist)
print(list(lst3))

