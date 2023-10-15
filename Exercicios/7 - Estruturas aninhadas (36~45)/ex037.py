# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um número inteiro: "))
conversion = int(input("Selecione o tipo de conversão ( 1 ) binário | ( 2 ) octal | ( 3 ) hexadecimal"))

if conversion == 1:
    print(f"A representação binária do seu número é: {bin(num)[2:]}")
elif conversion == 2:
    print(f"A representação octal do seu número é: {oct(num)[2:]}")
elif conversion == 3:
    print(f"A representação hexadecimal do seu número é: {hex(num)[2:]}")
else:
    print("Opção inválida, tente novamente!")