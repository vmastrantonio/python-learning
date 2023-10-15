# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0

while sexo != "M" and sexo != "F":
    sexo = str(input("Digite o seu sexo (M) ou (F): ")).upper()
    if sexo != "M" and sexo != "F":
        print("Opção inválida, tente novamente!")
    
print("Obrigado")