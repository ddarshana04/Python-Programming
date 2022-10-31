def TupleToList(t):
    list = []
    for i in t:
        if(type(i)!=type(0)):
            for j in i:
                list.append(j)
        else:
            list.append(i)
    return tuple(list)
t = ([10,50,60],[40,65])
print (TupleToList(t))                    