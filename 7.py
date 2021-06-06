def maxLength(string1, string2):
    if len(string1)> len(string2):
        print(string1)
    elif len(string2)> len(string1):
        print(string2)
    elif len(string1)== len(string2):
        print(string1)
        print(string2)
    else:
        print("wrong input")


maxLength("hi","hello")

maxLength("bishal","hamal")

maxLength("nine","nine")