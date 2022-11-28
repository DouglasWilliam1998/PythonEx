Salario=float(input())
if 0<=Salario<=2000:
    print("Isento")
elif 2000<Salario<=3000:
    Imposto=(Salario-2000)*0.08
    print(f"R$ {Imposto:.2f}")
elif 3000<Salario<=4500:
    Imposto=(Salario-2000)*0.18
    print(f"R$ {Imposto:.2f}")
elif Salario>4500:
    Imposto=(Salario-2000)*0.28
    print(f"R$ {Imposto:.2f}")



