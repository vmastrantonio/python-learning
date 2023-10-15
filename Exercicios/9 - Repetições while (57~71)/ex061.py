# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

ultimo = primeiro + (10 * razao)

termo = primeiro

while termo < ultimo:
    print(termo)
    termo += razao