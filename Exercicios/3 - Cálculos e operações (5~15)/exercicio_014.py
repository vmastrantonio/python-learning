# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

temp = int(input("Digite a temperatura em graus célsius: "))
temp_fahr = ((temp * 9) / 5) + 32

print(f"A temperatura {temp:.1f} ºC, em fahrenheit é {temp_fahr:.1f} ºF")