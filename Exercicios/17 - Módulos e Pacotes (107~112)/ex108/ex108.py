﻿# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores com um valor monetário formatado.

import moeda

num = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}")
print(f"Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}")
print(f"Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(num, 13))}")

# OBS: o intuito do exercicio era realmente fazer essa má prática de nomeação de funções e modularização para mostrar aos alunos.