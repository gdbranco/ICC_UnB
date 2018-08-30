n = int(input())
maior = float("-inf")
menor = float("inf")
while n:
    x, y = [int(k) for k in input().split()]
    if(x%2==0):
        x+=1
    t = 0
    while y:
        t+=x
        x+=2
        y-=1
    n-=1
    if(t > maior):
        maior = t
    if(t < menor):
        menor = t
    print(t)
print(maior)
print(menor)