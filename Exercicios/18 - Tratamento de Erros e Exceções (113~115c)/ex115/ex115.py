# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from pacote import visual as vs
from pacote import arquivo as arqv

if not arqv.verificaDatabase():
    arqv.criaDatabase()

def menu_principal():
    vs.cabecalho("MENU PRINCIPAL", 6)
    print(f"{vs.cor(1)}1 {vs.cor(4)}- Ver pessoas cadastradas{vs.cor(0)}")
    print(f"{vs.cor(1)}2 {vs.cor(4)}- Cadastrar nova pessoa{vs.cor(0)}")
    print(f"{vs.cor(1)}3 {vs.cor(4)}- Sair do sistema{vs.cor(0)}")
    print(f"{vs.cor(6)}{'-' * 30}{vs.cor(0)}")

    while True:
        escolha = int(input(f"{vs.cor(3)}Insira sua opção: {vs.cor(0)}"))
        if escolha == 1:
            arqv.lerDatabase()
            menu_principal()
            break
        elif escolha == 2:
            arqv.cadastrarDatabase()
            menu_principal()
            break
        elif escolha == 3:
            print(f"{vs.cor(2)}Obrigado, volte sempre!{vs.cor(0)}")
            break
        else:
            print(f"{vs.cor(1)}ERRO: Opção inválida, tente novamente.{vs.cor(0)}")
            continue

menu_principal()