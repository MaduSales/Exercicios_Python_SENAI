alunos = []
notas = []

for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    alunos.append(nome)
    nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
    notas.append(nota)

print(alunos, notas)
