# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt("Digite um n")

def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print(f"Erro! {n} não é um valor numérico.")

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")