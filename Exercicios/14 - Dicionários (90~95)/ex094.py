# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

escolha = True

lista_pessoas = []

while escolha:
    lista_pessoas.append({'nome': input("Nome: "), 'sexo': input("Sexo [H/M]: ").upper(), 'idade': int(input("Idade: "))})

    while True:
        opcao = input("Quer continuar? [S/N] ").lower()

        if opcao == 's':
            break
        elif opcao == 'n':
            escolha = False
            break
        else:
            print("Opção inválida, tente novamente")

totalIdade = 0
mulheres_cadastradas = []

for i in lista_pessoas:
    if i['sexo'] == 'M':
        mulheres_cadastradas.append(i['nome'])
    totalIdade += i['idade']

media_idade = totalIdade / len(lista_pessoas)

acima_media_idade = []

for i in lista_pessoas:
    if i['idade'] > media_idade:
        acima_media_idade.append(i['nome'])
    
print(f"Foram cadastradas {len(lista_pessoas)} pessoas.")
print(f"Média de idade do grupo: {media_idade:.1f}")
print(f"As mulheres cadastradas foram: {mulheres_cadastradas}")
print(f"Pessoas com idade acima da média: {acima_media_idade}")
