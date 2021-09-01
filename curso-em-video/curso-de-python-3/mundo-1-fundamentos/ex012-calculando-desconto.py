# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Preço do produto: R$'))
desconto = preco - (preco * 5/100)  # ou preco - (preco * 0.05)
print(f'O preço do produto com desconto de 5% é de R${desconto:.2f}')
