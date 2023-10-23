# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = { 'nome': input("Nome do aluno: "), 'media': float(input("Média do aluno: "))}

if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

for k,v in aluno.items():
    print(f"{k} é igual a {v}")
