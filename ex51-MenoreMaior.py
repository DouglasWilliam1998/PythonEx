numero1,numero2,numero3=map(float,input().split())
if numero1>numero2>numero3:
    print(f' O maior é :{numero1}')
    print(f' O menor é :{numero3}')
elif numero1>numero3>numero2:
    print(f' O maior é :{numero1}')
    print(f' O menor é :{numero2}')
elif numero2>numero1>numero3:
    print(f' O maior é :{numero2}')
    print(f' O menor é :{numero3}')
elif numero2>numero3>numero1:
    print(f' O maior é :{numero2}')
    print(f' O menor é :{numero1}')
elif numero3>numero1>numero2:
    print(f' O maior é :{numero3}')
    print(f' O menor é :{numero2}')
elif numero3>numero2>numero1:
    print(f' O maior é :{numero3}')
    print(f' O menor é :{numero1}')
else :
    print('Numeros repetidos')
