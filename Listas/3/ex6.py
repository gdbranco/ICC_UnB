n, m = [int(x) for x in input().split()]
mdc = None
for k in range(2,n+1):
    if(n%k==0 and m%k==0):
        mdc = k
print(mdc)