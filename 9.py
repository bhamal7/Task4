def showNumbers(limit):
    for i in range(limit+1):
        if (i % 2 == 0):
            print(i, "EVEN")
        else:
            print(i, "ODD")

showNumbers(int(input("Enter the limit number:")))