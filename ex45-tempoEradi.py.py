tempo=0
massaInicial=float(input())
massaFinal=massaInicial
while massaFinal>=0.5:
    massaFinal=massaFinal/2
    tempo +=50
print(f"Massa Inicial: {massaInicial} gramas")
print(f"Massa Inicial: {massaFinal} gramas")
horas= int(tempo/3600)
minutos=float((tempo%3600)/60)
segundos=float(((tempo%3600)%60))
print(f"{horas:.1f}: horas ")
print(f"{minutos:.1f}: minutos ")
print(f"{horas:.1f}: segundos ")