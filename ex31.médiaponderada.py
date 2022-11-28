a = int(input())
b = []
c = []
d = []

while len(b) < a:
    x = float(input())
    b.append(x)
b1 = ((b[0]*2)+(b[1]*3)+(b[2]*5))/10


while len(c) < a:
    y = float(input())
    c.append(y)
c1 = ((c[0]*2)+(c[1]*3)+(c[2]*5))/10


while len(d) < a:
    z = float(input())
    d.append(z)
d1 = ((d[0]*2)+(d[1]*3)+(d[2]*5))/10

print(f"{b1:.1f}")
print(f"{c1:.1f}")
print(f"{d1:.1f}")
