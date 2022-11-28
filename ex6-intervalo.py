Intervalo = float(input())
if Intervalo >= 0 and Intervalo <= 25:
    print("Intervalo [0,25]")
elif Intervalo > 25 and Intervalo <= 50:
    print("Intervalo (25,50]")
elif Intervalo > 50 and Intervalo <= 75:
    print("Intervalo (50,75]")
elif Intervalo > 75 and Intervalo <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
