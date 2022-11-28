v = []
positivo=0
while len(v) < 6:
    x = float(input())
    if x>0:
        positivo=positivo+1
    v.append(x)
print(f"{positivo} valores positivos")