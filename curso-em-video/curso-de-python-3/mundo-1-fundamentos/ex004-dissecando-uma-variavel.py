# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(algo))
print('É alfabético:', algo.isalpha())
print('Está capitalizado:', algo.istitle())
print('Está em maiúsculo:', algo.isupper())
print('Está em minúsculo:', algo.islower())
print('É numérico:', algo.isnumeric())
print('É alfanumérico:', algo.isalnum())
