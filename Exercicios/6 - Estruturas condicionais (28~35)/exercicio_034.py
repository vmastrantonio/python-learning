# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salary = float(input("Digite o salário do funcionário: "))

if salary > 1250:
    print(f"O salário irá receber 10% de aumento, e ficará R$ {salary * 1.1}")
else:
    print(f"O salário irá receber 15% de aumento, e ficará R$ {salary * 1.15}")