v = []
pares = 0
impares = 0
positivos = 0
negativos = 0
while len(v) < 5:
    x = int(input())
    if x % 2 == 0:
        pares = pares+1
        if x > 0:
            positivos = positivos+1
        if x < 0:
            negativos = negativos+1
    if x % 2 != 0:
        impares = impares+1
        if x > 0:
            positivos = positivos+1
        if x < 0:
            negativos = negativos+1
    v.append(x)

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativos(s)")
