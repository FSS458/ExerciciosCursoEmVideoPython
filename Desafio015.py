# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Por quantos dias esse carro foi alugado? "))
quilometragem = float(input("Quantos km esse caro percorreu? "))

precoTotal = dias * 60 + quilometragem * 0.15

print(f"O preço total a pagar pelo aluguel do carro é {precoTotal}R$")


