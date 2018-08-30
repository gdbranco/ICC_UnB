t = int(input())
while t:
    a, n = [int(x) for x in input().split()]
    s = 0
    for k in range(a, a+n):
        print(k,end="")
        if(k!=a+n):
            print(" ", end="")
        s+=k
    print(f"\n{s}")
    t-=1