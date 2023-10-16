# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

lista_palavras = "casa", "rato", "cachorro", "livro", "caneta", "gato", "mesa", "janela", "bola", "futebol"

for palavra in lista_palavras:
    print(f"As vogais da palavra {palavra} são:", end=" ")
    for letra in palavra:
        if letra.upper() in "AEIOU":
            print(letra, end=" ")
    print("")