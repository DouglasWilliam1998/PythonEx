numero=0
controle=int(input())
repeticao=0
while repeticao<controle:
    maior=(int(input()))
    if maior>numero:
        numero=maior
    repeticao=repeticao+1
print(numero)  