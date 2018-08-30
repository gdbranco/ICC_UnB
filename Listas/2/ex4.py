p, i = [int(x) for x in input().split()]
print(f"{p} {i}", end="")
if((p==i and i!=0) or (p+1)==i):
    print(" ok")
else:
    print(" errados")