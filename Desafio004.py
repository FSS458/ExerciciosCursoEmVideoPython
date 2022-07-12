# Programa utilizado para verificar o valor de um texto

teclado = input(print("Digite algo para ser verificado:"))
print(f"A classe do objeto digitado é: {type(teclado)}")
print("Só tem espaços? ", teclado.isspace())
print("É um número? ", teclado.isnumeric())
print("É um alfabético? ", teclado.isalpha())
print("É alfabético? ", teclado.isalnum())
print("Está em letras maiúsculas? ", teclado.isupper())
print("Está em letras minúsculas? ", teclado.islower() )

