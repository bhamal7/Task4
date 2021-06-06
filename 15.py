
def makeList(n):
    return n*n
   

lst= [1,2,3,4,5,6,7,8,9]
result = map(makeList,lst)
print(list(result))