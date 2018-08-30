h1, m1, h2, m2 = [int(x) for x in input().split()]
if(h2 > h1):
    h = h2-h1
elif(h2 < h1):
    h = 24 - (h1-h2)
else:
    h = 24

if(m2 > m1):
    m = m2-m1
elif(m2 < m1):
    m = 60 - (m1-m2)
    h -= 1
else:
    m = 0
print(f"O jogo durou {h} hora(s) e {m} minuto(s).")