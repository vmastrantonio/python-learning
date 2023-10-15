# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master

from datetime import datetime

birth_year = int(input("Digite o seu ano de nascimento: "))
current_year = datetime.now().year

age = current_year - birth_year

if age <= 9:
    category = "Mirim"
elif age <= 14:
    category = "Infantil"
elif age <= 19:
    category = "Junior"
elif age <= 20:
    category = "Senior"
else:
    category = "Master"
    
print(f"Sua categoria é: {category}")
