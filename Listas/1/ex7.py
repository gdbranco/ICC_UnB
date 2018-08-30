t = int(input())
print(t)
n100 = t//100
t = t%100
n50 = t//50
t = t%50
n20 = t//20
t = t%20
n10 = t//10
t = t%10
n5 = t//5
t = t%5
n2 = t//2
t = t%2
print(f"{n100} nota(s) de R$100,00")
print(f"{n50} nota(s) de R$50,00")
print(f"{n20} nota(s) de R$20,00")
print(f"{n10} nota(s) de R$10,00")
print(f"{n5} nota(s) de R$5,00")
print(f"{n2} nota(s) de R$2,00")
print(f"{t} nota(s) de R$1,00")