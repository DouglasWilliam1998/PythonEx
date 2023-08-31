lista=[]
tamanhodaLista=int(input())
for i in range(tamanhodaLista):
    notas=float(input())
    lista.append(notas)
print(lista)

soma=0
tamanho=0
for i in lista:
    soma+=i
    tamanho=i
media=(soma/tamanho)
print(media)