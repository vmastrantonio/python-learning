# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

qtdMaiores = 0
qtdMenores = 0

ano_atual = datetime.now().year

for i in range(1,8):
    nascimento = int(input("Insira o ano de nascimento de uma pessoa: "))
    if (ano_atual - nascimento) >= 18:
        qtdMaiores += 1
    else:
        qtdMenores += 1
    