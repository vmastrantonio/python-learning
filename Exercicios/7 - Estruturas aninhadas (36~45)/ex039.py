# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import datetime

year = int(input("Digite o ano do seu nascimento: "))
current_year = datetime.now().year
year_enlistment = year + 18

if current_year == year_enlistment:
    print("Que pena, está na hora de você se alistar!")
elif current_year < year_enlistment:
    print(f"Você ainda precisa esperar {year_enlistment - current_year} anos para poder se alistar!")
else:
    print(f"Já passou {current_year - year_enlistment} anos da data do seu alistamento")