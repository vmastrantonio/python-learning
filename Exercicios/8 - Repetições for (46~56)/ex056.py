# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# -> A média de idade do grupo.
# -> Qual é o nome do homem mais velho.
# -> Quantas mulheres têm menos de 20 anos.

qtdMulheres = 0
somaIdade = 0

idadeHomemVelho = 0
nomeHomemVelho = ''

for i in range(1, 5):
    print(f"----- {i}º pessoa -----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    
    if sexo == "M":
        if i == 1:
            idadeHomemVelho = idade
        else:
            if idade > idadeHomemVelho:
                idadeHomemVelho = idade
                nomeHomemVelho = nome
    else:
        if idade < 20:
            qtdMulheres += 1
    
    somaIdade += idade
    print(somaIdade)
    
mediaIdade = somaIdade / 4

print(f"A média de idade do grupo é de {mediaIdade} anos.")
print(f"O homem mais velho tem {idadeHomemVelho} anos e se chama {nomeHomemVelho}.")
print(f"Ao todo são {qtdMulheres} mulheres com menos de 20 anos.")