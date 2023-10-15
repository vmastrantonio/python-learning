# Crie um programa que faça o computaodr jogar jokenpô com você.

from random import randint

print("Jokenpô 1.0")

pc = randint(1,3)

print("(1) Pedra | (2) Papel | (3) Tesoura")
chosen = int(input("Escolha: "))

if chosen == pc:
    print("Empatou, ambos colocaram a mesma coisa.")
elif chosen == 1:
    if pc == 2:
        print("Você perdeu, você colocou pedra e o computador colocou papel!")
    if pc == 3:
        print("Você ganhou, você colocou pedra e computador colocou tesoura!")
elif chosen == 2:
    if pc == 1:
        print("Você ganhou, você colocou papel e o computador colocou pedra!")
    if pc == 3:
        print("Você perdeu, você colocou papel e o computador colocou tesoura!")
elif chosen == 3:
    if pc == 1:
        print("Você perdeu, você colocou tesoura e o computador colocou pedra!")
    if pc == 2:
        print("Você ganhou, você colocou tesoura e o computador colocou papel!")
else:
    print("Opção inválida, tente novamente.")