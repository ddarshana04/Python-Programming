sumD = 0;
num = int(input("Enter the number : "))
while(num!=0):
    temp = num%10
    sumD = sumD + temp
    num = int(num/10)
print("The sum of digits is : ", sumD)
