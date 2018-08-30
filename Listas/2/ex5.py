from math import ceil
m, d = (int(x) for x in input().split())
meses = [-1,31,28,31,30,31,30,31,31,30,31,30,31]
s = 1
for _ in range(1, meses[m]):
if(d%7 == 0):
    s += 1
d+=1
print(s)