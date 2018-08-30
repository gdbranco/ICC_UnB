p = float(input())
h = float(input())
imc = (p/h**2)
print(f"{imc:.2f}")
sobre = p - 24.9 * h**2
if(imc < 18.5):
    print("Baixo peso")
elif(18.5 <= imc < 24.9):
    print("Peso normal")
else:
    if(24.9 <= imc < 29.9):
        print("Sobrepeso")
    elif(29.9 <= imc < 34.9):
        print("Obesidade grau I")
    elif(34.9 <= imc < 39.9):
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")
    print(f"{sobre:.2f}")