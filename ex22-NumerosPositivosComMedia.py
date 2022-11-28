v = []
positivo=0
while len(v) < 6:
    x = float(input())
    if x>0:
        positivo=positivo+1
    v.append(x)
print(f"{positivo} valores positivos")
tamanho1=len(v)
tamanho=0
for i in range(tamanho1):
    tamanho=(tamanho+v[i])
    tamanho2=tamanho/positivo
print(tamanho2)