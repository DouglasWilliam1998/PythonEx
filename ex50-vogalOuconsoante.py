
escolhaLetra=input().upper()
if (escolhaLetra=='A' 
    or escolhaLetra=='E' 
    or escolhaLetra=='I' 
    or escolhaLetra=='O' 
    or escolhaLetra=='U'):
        print('Vogal')
elif escolhaLetra.isnumeric():
        print('Invalido')
else:
        print('Consoante')