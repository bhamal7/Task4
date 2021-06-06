
import functools

lst = [1,2,3,4,5,6,7]
result = functools.reduce(lambda i,j: 10*i+j,lst)
print(result)
