'''input1 = input("Enter the string as input: ")
lower = 0
upper = 0
for i in input1:
    if(i==i.upper()):
        upper+=1
    elif(i==i.lower()):
        lower+=1
    else:
        print("Enter only lower and upper letter string")

print("No. of Uppercase characters: ", upper)
print("No. of Lowercase characters: ", lower)
'''

def func(string):
    lower = 0
    upper = 0
    for i in string:
        if(i==i.upper()):
            upper+=1
        elif(i==i.lower()):
            lower+=1
        else:
            print("Enter only lower and upper letter string")
    print("No. of Uppercase characters: ", upper)
    print("No. of Lowercase characters: ", lower)
x = input("Enter the string as input: ")
func(x)