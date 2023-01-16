# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Qual seria o preço do produto que você gostaria de avaliar? "))

precoDesconto = preco * 95/100

print(f"O valor do seu produto, com 5% de desconto é {precoDesconto}R$")
