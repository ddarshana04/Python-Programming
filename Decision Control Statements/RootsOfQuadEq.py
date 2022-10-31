import math
p, q, r, d, r1, r2, rp, ip = None, None, None, None, None, None, None, None

print ("-----Enter the coefficients a, b and c----")
p = float (input ())
q = float (input ())
r = float (input ())
d = q * q - 4 * p * r

if (d > 0):
    r1 = (-q + math.sqrt(d)) / (2 * p)
    r2 = (-q - math.sqrt(d)) / (2 * p)
    print ("\nThe r1 = ", r1, " & r2 = ", r2)

elif d == 0:
    r1 = r2 = -q / (2 * p)
    print ("\nThe r1 = r2 = ", r1, ";\n")

else:
    rp = -q / (2 * p)
    ip = math.sqrt(-d) / (2 * p)
    print ("\nThe r1 = ", round(rp, 2), "+", round(ip, 2), "i & r2 = ", round(rp, 2), "-", round(ip, 2), "i")