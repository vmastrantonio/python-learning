# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

house_price = float(input("Qual o valor da casa? "))
salary = float(input("Quanto é o seu salário? "))
years = int(input("Em quantos anos você quer quitar o empréstimo? "))

months = years / 12
parcel = house_price / months
parcel_max = salary * 0.3

if parcel <= parcel_max:
    print(f"Parabéns, o seu empréstimo foi aprovado e a sua parcela será de {parcel}, para ser paga em {months} meses.")
else:
    print(f"Infelizmente o seu emprestimo foi recusado.")