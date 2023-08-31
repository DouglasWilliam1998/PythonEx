# Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 
# e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

numeroIdade=int(input())
soma=0

for i in range(0,numeroIdade):
    idade=int(input())
    soma=soma+idade
    mediaIdade=(soma/2)

        
if 0<mediaIdade<=25:
    print("Turma Jovem")

elif 25<mediaIdade<=60:
    print("Turma Adulta")

else:
    print("Turma Idosa")


