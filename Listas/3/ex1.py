n = int(input())
g = int(input())
while g != n:
    if(n > g):
        print("O número correto é maior.")
    elif(n < g):
        print("O número correto é menor.")
    g = int(input())
print("Parabéns! Você acertou.")