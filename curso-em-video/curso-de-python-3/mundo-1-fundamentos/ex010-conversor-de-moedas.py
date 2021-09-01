# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Dinheiro na carteira: R$'))
dolar = carteira / 5.16
print(f'Com R${carteira:.2f} se compra US${dolar:.2f}')
