crescimentoA=(80000*0.03)
print(crescimentoA)
crescimentoB=(200000*0.015)
print(crescimentoB)
anos=0
while crescimentoA<crescimentoB:
    anos=int(input())
    crescimentoA=anos*crescimentoA
print(f'São necessários {anos}')





