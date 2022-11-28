alcool = 0
gasolina = 0
diesel = 0
menu = 0

while menu != 4:

    menu = int(input())
    if menu == 1:
        alcool = alcool+1
    elif menu == 2:
        gasolina = gasolina+1
    elif menu == 3:
        diesel = diesel+1
    else:
        print("Digite outro número")
print("MUITO OBRIGADO")
print(f" Alcool: {alcool}")
print(f" Gasolina: {gasolina}")
print(f" Diesel: {diesel}")

