# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 até 30: Sobrepeso
# - Entre 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

weight = float(input("Digite o seu peso em KGs (Exemplo: 76.4): "))
height = float(input("Digite sua altura em M (Exemplo: 1.82): "))

imc = weight / height ** 2

if imc <= 18.5:
    print(f"Seu imc é {imc:.1f}, você está abaixo do peso.")
elif imc <= 25:
    print(f"Seu imc é {imc:.1f}, você tem um peso ideal.")
elif imc <= 30:
    print(f"Seu imc é {imc:.1f}, você está com sobre peso.")
elif imc <= 40:
    print(f"Seu imc é {imc:.1f}, você está com obesidade.")
else:
    print(f"Seu imc é {imc:.1f}, você está com obesidade mórbida.")