# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leInteFloat(msgInt, msgReal):
    try:
        validador = 0
        numInt = int(input(msgInt))
        validador == 1
        numFloat = float(input(msgReal))
    except ValueError:
        if validador == 0:
            print("ERRO: O tipo de valor não é um número inteiro.")
        else:
            print("ERRO: O tipo de valor não é um número real.")
    except (KeyboardInterrupt):
        print("ERRO: O usuário preferiu não inserir um número.")
    except Exception as erro:
        print(erro.__class__)

leInteFloat("Digite um número inteiro: ", "Digite um número real: ")