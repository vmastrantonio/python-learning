﻿# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

num = float(input("Digite o preço: R$ "))
print(f"A metade de {num} é {moeda.metade(num, True)}")
print(f"O dobro de {num} é {moeda.dobro(num, True)}")
print(f"Aumentando 10%, temos {moeda.aumentar(num, 10, True)}")
print(f"Reduzindo 13%, temos {moeda.diminuir(num, 13, True)}")