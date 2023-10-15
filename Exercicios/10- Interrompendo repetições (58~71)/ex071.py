# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

cont = 0

while True:
    saque = int(input("Informe o valor a ser sacado: "))
    
    while saque > 0:
        
        if cont == 0:
            valor_cedula = 50
        elif cont == 1:
            valor_cedula = 20
        elif cont == 2:
            valor_cedula = 10
        elif cont == 3:
            valor_cedula = 1
        
        quantidade_cedula = saque // valor_cedula
        
        if quantidade_cedula > 0:
            saque = saque - quantidade_cedula * valor_cedula
            print(f"Total de {quantidade_cedula} cédulas de R$ {valor_cedula}")
            
        cont += 1
    break