# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))

ultimo = primeiro + (10 * razao)

Working = True

termo = primeiro

while Working:
    while termo < ultimo:
        print(termo)
        termo += razao
    novosTermos = int(input("Quer ver mais quantos termos? "))
    if novosTermos == 0:
        Working = False
    else:
        ultimo = ultimo + (novosTermos * razao)