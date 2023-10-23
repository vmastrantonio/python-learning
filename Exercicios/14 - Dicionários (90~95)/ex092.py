# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

inss = {'nome': input("Digite o nome: "), 'idade': datetime.now().year - int(input("Digite o ano de nascimento: ")), 'ctps': int(input("Digite a carteira de trabalho: "))}

if inss['ctps'] != 0:
    inss['contratacao'] = int(input("Digite o ano de contratação: "))
    inss['salario'] = int(input("Digite o seu salário: "))
    inss['idade_aposentar'] = (35 - (datetime.now().year - inss['contratacao'])) + inss['idade']

for k,v in inss.items():
    print(f"{k} tem o valor {v}")