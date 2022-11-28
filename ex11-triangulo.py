from posixpath import split


valores = input().split()
a, b, c = valores
a = float(a)
b = float(b)
c = float(c)

#if a > 0 and b > 0 and c > 0:
if a+b > c or c+a > b or b+c > a:
    print(f"Perimetro = {a+b+c:.1f}")
else:
    print(f"Area = {((a+b)*c)/2:.1f}")
