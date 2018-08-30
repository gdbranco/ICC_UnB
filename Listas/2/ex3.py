a = float(input())
b = float(input())
c = float(input())
if(b>a and b>c):
    a, b = b, a
elif(c>a and c>b):
    a, c = c, a
if(a>=b+c):
    print("NAO FORMA TRIANGULO")
elif(a==b and a==c):
    print("TRIANGULO EQUILATERO")
elif(a**2 == b**2 + c**2):
    print("TRIANGULO RETANGULO")
elif((a==b and a!=c) or (a==c and a!=b) or (c==b and c!=a)):
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")