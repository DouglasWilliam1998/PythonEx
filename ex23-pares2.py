v = []
pares=0
while len(v) < 5:
    x = int(input())
    if x%2==0:
        pares=pares+1
    v.append(x)
print(f"{pares} valores pares")