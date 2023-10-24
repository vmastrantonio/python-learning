# Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva("Olá, Mundo!")
# Saída: ------------
#         Olá, mundo       
#        ------------

def escreva(msg):
    tamanho = len(msg)
    print("~" * tamanho)
    print(msg)
    print("~" * tamanho)

escreva("Olá, Mundo!")