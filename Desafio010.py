# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input("Quanto dinheiro você possui na sua carteira? ")) # Moeda considerada na carteira = real
dolar = 5.42
conversao = carteira/dolar

print(f"Você pode comprar U${conversao} com R${carteira}")



