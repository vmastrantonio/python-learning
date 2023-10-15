# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

num1 = int(input("Digite sua primeira nota: "))
num2 = int(input("Digite sua segunda nota: "))

average = (num1 + num2) / 2

if average >= 7:
    print(f"Você está aprovado com uma média de {average}!")
elif average >= 5:
    print(f"Você vai precisar fazer recuperação, sua média foi {average}")
else:
    print(f"Você foi reprovado, sua média é de {average}")
