altura = float(input("Qual é a altura da sua parede em metros? "))
largura = float(input("Qual é a largura da sua parede em metros? "))

area = altura * largura
baldes = area/2

print("Sua parede possui uma área de {}m² e você precisa de {} baldes de tinta para pintá-la completamente!".format(area, baldes))

