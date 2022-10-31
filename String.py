import math
s1 = "sheep"
s2 = "horse"
m1 = math.floor(len(s1)/2)
m2 = math.floor(len(s2)/2)
result = s1[-1] + s2[-1] + s1[m1] + s2[m2] + s1[0] + s2[0]
print(result)