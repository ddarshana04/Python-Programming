import math
while(1):
    num = int(input("Enter a number "))
    if(num==999):
        break
    elif num<0:
        print("Square root of negative number is not computed")
        continue
    else:
        print("Square root of ", num, " = ", math.sqrt(num))

