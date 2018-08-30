m = int(input())
fat = 1
fib1 = 1
fib2 = 1
fib = 1
for k in range(1, m+1):
    fat*=k
    if(k!=1 and k!=2):
        fib = fib1 + fib2
        fib1, fib2 = fib, fib1
print(fib,fat,end="")
if(fib%2==0):
    print(f" {fib1+fib2 - fib}")