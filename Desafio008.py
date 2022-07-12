#  Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medidaM = float(input("Qual é a medida em metro(s) que você deseja converter? "))

medidacm = medidaM * 100
medidamm = medidaM * 1000

print(f" A medida que você forneceu é {medidaM}m \n Sua conversão para cm é {medidacm}cm \n Sua conversão para milímetros é {medidamm}mm")
