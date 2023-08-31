limitador=10
contador=0
pares=0
impares=0
while contador<limitador:
    x=int(input())
    if x%2==0:
        pares=pares+1
    else:
        impares=impares+1
    contador=contador+1
print(f"Números pares : {pares}")
print(f"Números ímpares : {impares}")