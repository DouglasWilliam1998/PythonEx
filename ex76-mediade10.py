num_alunos = 10
notas_alunos = []

for i in range(num_alunos):
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    notas_alunos.append(media)

num_aprovados = 0
for media in notas_alunos:
    if media >= 7.0:
        num_aprovados += 1

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {num_aprovados}")
