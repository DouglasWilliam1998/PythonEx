idades=100
contador=0
soma=0
while idades!=0:
    idades=0
    idades=int(input())
    soma=idades+soma  
    if idades==0:
        break
    contador+=1
print(soma/contador)    