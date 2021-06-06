#(i)
def foo():
    try:
        return 1
    finally:
        return 2

k = foo()
print(k)

# the output of the above code is 2


#(ii)

# the above code will not give output becasue the name f and x are undefined.