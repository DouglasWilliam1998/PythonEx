entrada=int(input())
dentro=0
fora=0
v = []
while len(v) < entrada:
    x = int(input())
    if 10<=x<=20:
        dentro=dentro+1
    else:
        fora=fora+1
    v.append(x)
print(f"{dentro} in")
print(f"{fora} out")