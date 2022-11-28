from contextlib import nullcontext


ddd=int(input())
a=nullcontext
if ddd==11:
    a="São Paulo"
if ddd==61:
    a="Brasilia"
if ddd==71:
    a="Salvador"
if ddd==21:
    a="Rio de Janeiro"
if ddd==32:
    a="Juiz de Fora"
if ddd==19:
    a="Campinas"
if ddd==27:
    a="Vitoria"
if ddd==31:
    a="Belo Horizonte"
print(a)