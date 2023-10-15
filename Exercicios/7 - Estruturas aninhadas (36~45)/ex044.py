# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros;

price = float(input("Digite o preço do produto: R$ "))

print("Escolha a condição de pagamento: (1) à vista no dinheiro | (2) à vista no cartão | (3) 2x no cartão | (4) 3x ou mais no cartão")
chosen = int(input())

if chosen == 1:
    print(f"A vista no dinheiro, o produto tem 10% de desconto e fica por R$ {price * 0.9:.2f}")
elif chosen == 2:
    print(f"A vista no cartão, o produto tem 5% de desconto e fica por R$ {price * 0.95:.2f}")
elif chosen == 3:
    print(f"Em até 2x no cartão, o preço continua R$ {price:.2f}")
elif chosen == 4:
    print(f"Em 3x ou mais, possuí juros de 20% e fica por R$ {price * 1.2:.2f}")