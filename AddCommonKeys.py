from collections import Counter
d1 ={'a': 100, 'b':200, 'c':300, 'd': 400}
d2 =  {'a':50, 'b':20, 'c':100}
result = Counter (d1) + Counter (d2)
print (result)