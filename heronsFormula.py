a = float(input("enter 1st side: "))
b = float(input("enter 2nd side: "))
c = float(input("enter 3rd side: "))
s = (a + b + c)/2  #Semi-perimeter
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  #area
print ('Area of triangle: %0.4f' %area)