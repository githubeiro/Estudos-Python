# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário: R$'))
novo_salario = salario + (salario * 0.15)
print(f'O salário com 15% de aumento é de R${novo_salario:.2f}')
