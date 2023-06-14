# Algoritmo contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área (A = (base x altura)/2).

def triangulo():
  base = int(input('Insira o valor da base do triângulo: '))
  altura = int(input('Insira o valo da altura do triângulo: '))
  area = (base * altura ) / 2
  print('A área do triângulo é',area)
  return area

def main():
  triangulo()

main()
