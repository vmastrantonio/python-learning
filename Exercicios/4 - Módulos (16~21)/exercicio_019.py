# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome escolhido.

from random import choice

aluno1 = str(input("Insira o nome do primeiro aluno: "))
aluno2 = str(input("Insira o nome do segundo aluno: "))
aluno3 = str(input("Insira o nome do terceiro aluno: "))
aluno4 = str(input("Insira o nome do quarto aluno: "))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

print(f"O aluno escolhido para apagar o quadro foi o(a) {choice(lista_alunos)}")