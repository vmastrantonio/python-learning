# Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(* num):
    count = 1
    for i in num:
        if count == 1:
            maior = num[0]
        else:
            if i > maior:
                maior = i
        count += 1
    print(f"O maior número foi o {maior}")

maior(1,3,5,6,2,5,3,7,4,1)