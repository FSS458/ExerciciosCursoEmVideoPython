dias = int(input("Por quantos dias esse carro foi alugado? "))
quilometragem = float(input("Quantos km esse caro percorreu? "))

precoTotal = dias * 60 + quilometragem * 0.15

print(f"O preço total a pagar pelo aluguel do carro é {precoTotal}R$")


