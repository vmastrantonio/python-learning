# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres = 0

while True:
    idade = int(input("Digite a idade de uma pessoa: "))
    
    while sexo not in "MF":
        sexo = str(input("Digite o sexo dessa pessoa [M/F]: ")).strip().upper()
    
    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade < 20:
        mulheres += 1
    
    while resposta not in "SN":
        resposta = str(input("Quer cadastrar mais uma pessoa? [S/N]: ")).strip().upper()
    
    if resposta == "N":
        break
    
print(f"Você cadastrou {maiores} pessoa(s) que são maior(es) de idade.")
print(f"Você cadastrou {homens} homen(s).")
print(f"Você cadastrou {mulheres} mulher(es) com menos de 20 anos.")