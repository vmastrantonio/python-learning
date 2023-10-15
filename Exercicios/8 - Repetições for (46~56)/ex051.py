# Desenvovla um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

primeiro = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
ultimo = primeiro + (10 * razao)

for c in range(primeiro, ultimo, razao):
    print(c)