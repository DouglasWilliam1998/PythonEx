numero=0
numero1=float('inf')
controle=int(input())
repeticao=0
while repeticao<controle:
    maior=(int(input()))
    if maior>0 and maior<1000:
        if maior>numero:
            numero=maior
        if(maior<numero1):
            numero1=maior
        repeticao=repeticao+1
    else:
        print("Número invalído")
print(numero)
print(numero1)  