# Faça um programa que leia um número qualquer e mostre o seu fatorial.


num = int(input("Insira um número: "))

cont = num
fatorial = num

while cont > 1:
    cont -= 1
    fatorial *= cont
    
print(f"O fatorial de {num} é {fatorial}")
    
    