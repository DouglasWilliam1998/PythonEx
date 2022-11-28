Nota1=float(input())
Nota2=float(input())
Nota3=float(input())
Nota4=float(input())
media=((Nota1*2)+(Nota2*3)+(Nota3*4)+Nota4)/10
print(f"Media: {media:.1f}")
if media>=7.0:
    print("Aluno aprovado.")
elif 5<media<6.9:
    print("Aluno em exame")
    NotaDoExame=float(input())
    print(f"Nota do exame: {NotaDoExame:.1f}")
    media=(media+NotaDoExame)/2
    if media>=5:
        print(f"Aluno aprovado.")
        print(f"Media final: { media:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final{ media:.1f}")
else:
    print("Aluno reprovado.")

    
