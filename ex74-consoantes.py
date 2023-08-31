controle=int(input())
soma=0
numerodeConsoantes=0
listadeVogais=[]
while (soma<controle):
    escolhaLetra=input().upper()
    if (escolhaLetra=='A' 
        or escolhaLetra=='E' 
        or escolhaLetra=='I' 
        or escolhaLetra=='O' 
        or escolhaLetra=='U'):
            print(f'Vogal: {escolhaLetra}')
            soma+=1
            listadeVogais.append(escolhaLetra)
    elif escolhaLetra.isnumeric():
            print('Entrada Inválida')
    else:
            print(f'Consoante: {escolhaLetra}')
            numerodeConsoantes+=1
print(f"Número de Consoantes: {numerodeConsoantes}")
print(listadeVogais)