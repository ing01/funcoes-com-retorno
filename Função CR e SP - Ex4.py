##Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área (A = lado2). Observação o número 2 significa ao quadrado.

def quadrado():
  lado = int(input('Insira o valor do lado do quadrado: '))
  area = lado ** 2
  print('O valor da área do quadrado é',area)
  return area

def main():
  quadrado()

main()
