nome=input()
senha=input()
while senha==nome:
    senha=input("Digite outra senha:")
print(f"Nome:{nome}")
print(f"Senha:{senha}")