lista=[]
tamanhodaLista=int(input())
while len(lista)<tamanhodaLista:
    valores=int(input())
    lista.append(valores)
print(lista)

listaReversa=[]
for i in range(tamanhodaLista,0,-1):
    listaReversa.append(i)
print(listaReversa)