# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase qualquer: ")).replace(" ", "").upper()

inverso = ''

for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
    
if frase == inverso:
    print("É palindromo")
else:
    print("Não é")
    
    