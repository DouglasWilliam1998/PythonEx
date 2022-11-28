a, b, c = 1,1,1
entrada = int(input())
repetidor = 0
while repetidor < entrada :
    print(f"{a} {b**2} {c**3}")
    print(f"{a} {b**2+1} {c**3+1}")
    a=a+1
    b+=1
    c+=1
    repetidor+=1