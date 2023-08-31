numerodeTumas=int(input())
soma=0
controle=0
while controle<numerodeTumas:
    numerodeAlunos=int(input())
    if 0<numerodeAlunos<=40:
        soma+=numerodeAlunos
        controle+=1
    else:
        print("Número Inválido")
media=soma/numerodeTumas
print(media)
