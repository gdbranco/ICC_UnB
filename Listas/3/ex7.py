n = int(input())
m = 0
prime = True
while prime:
    m+=1
    r = n*m + 1
    for i in range(2, r):
        if(r % i == 0):
            prime = False
            break
print(m)