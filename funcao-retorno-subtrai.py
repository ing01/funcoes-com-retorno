# Algoritmo contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.

def subtrair():
  num1 = int(input('Insira o primeiro número: '))
  num2 = int(input('Insira o segundo número: '))
  sub = num1 - num2
  print('O resultado da subtração é',sub)
  return sub

def main():
  subtrair()

main()
