# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno_1 = str(input("Digite o nome do primeiro aluno: "))
aluno_2 = str(input("Digite o nome do segundo aluno: "))
aluno_3 = str(input("Digite o nome do terceiro aluno: "))
aluno_4 = str(input("Digite o nome do quarto aluno: "))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista_alunos)

print(f"1º {lista_alunos[0]}\n2º {lista_alunos[1]}\n3º {lista_alunos[2]}\n4º {lista_alunos[3]}")

