N = int(input())
cont = 0
a,b,c = 1,1,1
while cont < N:
    print('{0} {1} {2} '.format(a,b,c))
    a=a+1
    b=a**2
    c=a**3
    cont+=1