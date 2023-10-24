# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indica o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial


def fatorial(num, show=False):
    fact = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fact *= c
    return fact

print(fatorial(10, True))