# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do grêmio.

tabela = ("Botafogo", "Bragantino", "Grêmio", "Palmeiras", "Flamengo", "Fortaleza", "Fluminense", "Athletico-PR", "Atlético-MG", "São Paulo", "Cuiabá", "Internacional", "Cruzeiro", "Corinthians", "Santos", "Bahia", "Vasco da Gama", "Goiás", "Coritiba", "América-MG")

primeiros5 = tabela[0:5]
ultimos4 = tabela[-4:]
ordem_alfabetica = sorted(tabela)
posicao_gremio = tabela.index("Grêmio") + 1

print(f"Os 5 primeiros são: {primeiros5}")
print(f"Os 4 ultimos são: {ultimos4}")
print(f"Times em ordem alfabética: {ordem_alfabetica}")
print(f"O grêmio está na {posicao_gremio}ª posição")