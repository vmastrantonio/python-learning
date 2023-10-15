# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

ultimo = primeiro + (10 * razao)

Working = True

pa = primeiro

while Working:
    while pa < ultimo:
        print(pa)
        pa += razao
    termos = int(input("Quer ver mais quantos termos? "))
    if termos == 0:
        Working = False
    else:
        ultimo = ultimo + (termos * razao)