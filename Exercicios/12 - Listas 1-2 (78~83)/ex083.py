# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite uma expressão com parênteses: ")
parenteses = []

for caractere in expressao:
    if caractere == "(":
        parenteses.append(caractere)
    elif caractere == ")":
        if not parenteses:
            print("O fechamento dos parênteses está na ordem errada!")
            break
        parenteses.pop()
else:
    if not parenteses:
        print("Expressão válida, todos os parênteses estão na ordem correta.")
    else:
        print("Número de parênteses abertos não corresponde ao número de parênteses fechados.")