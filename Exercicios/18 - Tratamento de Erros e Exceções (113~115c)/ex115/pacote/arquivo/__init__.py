from pacote import visual as vs

def verificaDatabase():
    try:
        arquivo = open("database.txt", "rt")
        arquivo.close()
    except Exception as error:
        print(f"{vs.cor(1)}ERRO: Código do erro: {error.__class__}{vs.cor(0)}")
        return False
    else:
        return True

def criaDatabase():
    try:
        database = open("database.txt", "wt+")
        database.close()
    except Exception as error:
        print(f"{vs.cor(1)}ERRO: Código do erro: {error.__class__}{vs.cor(0)}")
    
def lerDatabase():
    try:
        database = open("database.txt", "rt")
    except Exception as error:
        print(f"{vs.cor(1)}ERRO: Código do erro: {error.__class__}{vs.cor(0)}")
    else:
        vs.cabecalho("PESSOAS CADASTRADAS", 6)
        for linha in database:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<20}{dado[1]:>3} anos")
        database.close()
    
def cadastrarDatabase():
    vs.cabecalho("NOVO CADASTRO", 6)
    while True:
        try:
            nome = ""
            while nome == "":
                nome = input(f"{vs.cor(3)}Nome: {vs.cor(0)}")
                if nome == "":
                    print(f"{vs.cor(1)}ERRO: O nome não pode estar vazio.{vs.cor(0)}")
            idade = int(input(f"{vs.cor(3)}Idade: {vs.cor(0)}"))
        except (ValueError):
            print(f"{vs.cor(1)}ERRO: Idade inválida, insira apenas um número inteiro.{vs.cor(0)}")
        except Exception as error:
            print(f"{vs.cor(1)}ERRO: Erro do tipo {error.__class__}")
        else:
            try:
                database = open("database.txt", "at")
            except Exception as error:
                    print(f"{vs.cor(1)}ERRO: Houve um erro ao abrir o arquivo, código do erro: {error.__class__}{vs.cor(0)}")
            else:
                try:
                    database.write(f"{nome};{idade}\n")
                except Exception as error:
                        print(f"{vs.cor(1)}ERRO: Houve um erro ao cadastrar uma nova pessoa, código do erro: {error.__class__}{vs.cor(0)}")
                else:
                    print(f'{vs.cor(1)}"{nome}" {vs.cor(2)}adicionado ao banco de dados!{vs.cor(0)}')
                    break