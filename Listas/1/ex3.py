d = int(input())
vx = 60/3.6
vy = 75/3.6
vm = vy - vx
d *= 1000
print(f"{int(d/vm/60)} minutos")