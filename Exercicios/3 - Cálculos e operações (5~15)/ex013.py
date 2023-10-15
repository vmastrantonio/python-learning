# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = int(input("Digite o salário: "))
salario_aumento = salario + (salario * 0.15)

print(f"O salário, com 15% de aumento fica R$ {salario_aumento:.2f}")