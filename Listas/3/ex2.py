n = int(input())
t = 0
s = 0
maior = n
while n != 0:
    t+=1
    s+=n
    if(n > maior):
        maior = n
    n = int(input())
print(t)
print(maior)
print(f"{s/t:.2f}")