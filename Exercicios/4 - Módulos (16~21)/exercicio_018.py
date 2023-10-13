# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = radians(float(input("Digite o ângulo: ")))

sen = sin(angulo)
cos = cos(angulo)
tan = tan(angulo)

print(f"O seno do ângulo é {sen:.2f}, o cosseno é {cos:.2f} e a tangente é {tan:.2f}")