def leiaDinheiro(txt):
    dado = input(f"{txt}").replace(",", ".").strip()
    if dado.isalpha() or dado == "":
        print(f'\033[0;31mERRO: O valor "{dado}" não é um valor numérico.\033[m')
    else:
        return float(dado)