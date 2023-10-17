# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input("Insira um número inteiro, ou -1 para parar: "))
    if not num in lista:
        lista.append(num)
    else:
        print(f"Esse número já existe nessa lista.")
        
    while True:
        continuar = input("Quer continuar? [S/N] ").strip().lower()
        if continuar in ["s", "n"]:
            break
        else:
            print("Resposta inválida. Por favor, digite 'S' para continuar ou 'N' para parar.")
    
    if continuar == "n":
        break

print(f"Você digitou os valores: {sorted(lista)}")
    