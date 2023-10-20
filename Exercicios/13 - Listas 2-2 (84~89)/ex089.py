# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

matriz_alunos = []

while True:
    nome_aluno = input("Informe o nome do aluno: ")
    nota_1 = float(input("Informe a primeira nota: "))
    nota_2 = float(input("Informe a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    lista_temporaria = []
    lista_temporaria_notas = []
    
    lista_temporaria.append(nome_aluno)

    lista_temporaria_notas.append(nota_1)
    lista_temporaria_notas.append(nota_2)
    lista_temporaria_notas.append(media)

    lista_temporaria.append(lista_temporaria_notas)
    matriz_alunos.append(lista_temporaria)

    if input("Quer continuar? [S/N] ").strip().lower() == "n":
        break


print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-" * 30)
for pos, aluno in enumerate(matriz_alunos):
    print(f"{pos:<4} | {aluno[0]:<10} | {aluno[1][2]:>8.1f}")

while True:
    mostrar_notas = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if mostrar_notas == 999:
        break
    else:
        print(f"Notas de {matriz_alunos[mostrar_notas][0]} são {matriz_alunos[mostrar_notas][1][0]} e {matriz_alunos[mostrar_notas][1][2]}.")