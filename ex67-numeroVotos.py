votos=int(input())
candidato1=0
candidato2=0
candidato3=0
controle=0
while controle<votos:
    voto1=int(input())
    if voto1>=1 and voto1<=3:
        if voto1==1:
            candidato1=candidato1+1
        elif voto1==2:
            candidato2=candidato2+1
        elif voto1==3:
            candidato3=candidato2+1
        controle=controle+1
    else:
        print("Voto invalído")
print(candidato1,candidato2,candidato3)
