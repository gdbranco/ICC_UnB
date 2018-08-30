x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(y) for y in input().split()]
c = complex(input())
from math import sqrt
d1 = ((x2-x1)**2 + (y1-y2)**2)**0.5
d2 = sqrt(c.real**2 + c.imag**2)
print(f"{d1:.4f}")
print(f"{d2:.4f}")