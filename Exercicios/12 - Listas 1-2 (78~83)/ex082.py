# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, recpectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = []

while True:
    numeros.append(int(input("Digite um número: ")))

    while True:
        escolha = str(input("Deseja adicionar outro número? [S/N]: "))
        if escolha in "sn":
            break
        else:
            print("Opção inválida, utilize apenas [S/N]!")
            
    if escolha == "n":
        break
    
impares = []
pares = []

for item in numeros:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
        
print(f"Lista completa: {numeros}")
print(f"Números impares: {impares}")
print(f"Números pares: {pares}")