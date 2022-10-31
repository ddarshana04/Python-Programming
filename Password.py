pw = input("Enter password: ")
flag = 1
a = u = 0
if len(pw) < 8:
    flag = 0
if pw[0].isdigit():
    flag = 0
for i in pw:
    if(i.isalpha()):
        a+=1
    if(i.isupper()):
        u+=1
if(flag ==1 and u>=1 and a>=1):
    print("Valid Password")
else:
    print("Invalid Password")                         