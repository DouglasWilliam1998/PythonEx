numerodeValores=int(input())
listaPar=[]
listaImpar=[]
for i in range(numerodeValores):
    numero=int(input())
    if (numero%2==0):
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print(listaPar)
print(listaImpar)