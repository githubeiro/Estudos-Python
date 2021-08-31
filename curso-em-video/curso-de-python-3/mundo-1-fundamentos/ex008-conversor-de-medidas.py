# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Infome um valor em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'{medida}m equivale a {cm:.0f}cm')
print(f'{medida}m equivale a {mm:.0f}mm')
