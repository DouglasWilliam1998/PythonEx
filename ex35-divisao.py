cont = int(input())
for i in range(cont):
    x, y = list(map(float, input().split()))
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print('divisao impossivel')
