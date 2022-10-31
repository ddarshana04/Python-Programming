def Swap_string(str1, str2):
    str1 = str1 + str2;
    str2 = str1[0 : (len(str1)- len(str2))]
    str1 = str1[len(str2):]
    print("After swapping: ")
    print("String 1: " + str1+ " & String 2: " + str2)

str1 = input("Enter String 1:")
str2 = input("Enter String 2:") 
print ("Before swapping: ")
print("String 1: " + str1+ " & String 2: " +str2)
Swap_string(str1,str2)
