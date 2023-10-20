# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

pilha = []

expressao = input("Insira uma expressão matemática utilizando parênteses: ")

for crtr in expressao:
    if crtr == '(':
        pilha.append(crtr)
    elif crtr == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(crtr)
            break

if len(pilha) == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")