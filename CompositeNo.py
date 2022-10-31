def composite(a,b):
    for i in range(a, b+1):
        c = 0
        for j in range(2, i +1):
            if(i%j==0):
                c+=1
            if c>1:
                list.append(i)

a = int(input("Start range: ")) 
b = int(input("End range: "))
list = []
composite(a,b)
print("Composite numbers btwn ",a," and ",b," are: ")
print (list)              
