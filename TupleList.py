def Even_sum(list):
    sum = 0
    for i in list:
        if(i%2 ==0):
            sum += i
            print("Sum of even numbers: ", sum)
MyList = []
n = int(input("Number of elements you want in list: "))
for i in range(1, n+1):
    value = int(input("Enter values: "))
    MyList.append(value)
print ("List: ")
print (MyList)
Even_sum(MyList) 
