t1 = (11,3)
t2 = (15,70)
print("Tuple 1: " + str(t1))
print("Tuple 2: " + str(t2))
result = [(i, j) for i in t1 for j in t2]
result = result + [(i,j) for i in t1 for j in t1]
print ("Pairs of combinations: " + str(result))
