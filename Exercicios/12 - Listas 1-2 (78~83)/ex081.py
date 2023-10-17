# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista

valores = []

while True:
    valores.append(int(input("Digite um número: ")))

    while True:
        escolha = str(input("Deseja adicionar outro número? [S/N]: ")).strip().lower()
        if escolha in "sn":
            break
        else:
            print(f"Opção inválida, utilize [S/N]: ")
    if escolha == "n":
        break
            
valores.sort(reverse=True)

print(f"Foram digitados {len(valores)} números.")
print(f"Lista decrescente: {valores}")

if 5 in valores:
    print("O número 5 foi digitado e está na lista.")
else:
    print("O número 5 não foi digitado, portanto não está na lista.")