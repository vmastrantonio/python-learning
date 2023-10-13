# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de até 200Km e R$ 0.45 para viagens mais longas.

distance = float(input("Digite a distância da viagem, em kilometros: "))

if distance <= 200:
    km_price = 0.50
else:
    km_price = 0.45
    
print(f"O preço da viagem é R$ {distance * km_price:.2f}")