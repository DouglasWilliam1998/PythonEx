salario=float(input())
if 0<salario<=400:
    Reajuste=salario*0.15
    NovoSalario=salario+Reajuste
    print(f"Novo salario: {NovoSalario:.2f}")
    print(f"Reajuste ganho: {Reajuste:.2f}")
    print(f"Em percentual: 15%")
elif 400.01<=salario<=800:
    Reajuste=salario*0.12
    NovoSalario=salario+Reajuste
    print(f"Novo salario: {NovoSalario:.2f}")
    print(f"Reajuste ganho: {Reajuste:.2f}")
    print(f"Em percentual: 12%")
elif 800.01<=salario<=1200:
    Reajuste=salario*0.10
    NovoSalario=salario+Reajuste
    print(f"Novo salario: {NovoSalario:.2f}")
    print(f"Reajuste ganho: {Reajuste:.2f}")
    print(f"Em percentual: 10%")
elif 1200.01<=salario<=2000:
    Reajuste=salario*0.07
    NovoSalario=salario+Reajuste
    print(f"Novo salario: {NovoSalario:.2f}")
    print(f"Reajuste ganho: {Reajuste:.2f}")
    print(f"Em percentual: 7%")
elif salario>2000:
    Reajuste=salario*0.04
    NovoSalario=salario+Reajuste
    print(f"Novo salario: {NovoSalario:.2f}")
    print(f"Reajuste ganho: {Reajuste:.2f}")
    print(f"Em percentual: 4%")

