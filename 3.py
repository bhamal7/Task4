def function(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist

print(function([1,2,3,3,3,3,4,0,2,33,45,2,1,1,1,3,2,4,5,5]))
