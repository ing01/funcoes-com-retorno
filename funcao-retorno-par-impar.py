# Algoritmo contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.

def verificar():
  num = int(input('Insira um número: '))
  if num % 2 == 0:
    print('É Par')
  else:
    print('É ímpar')
  return num

def main():
  verificar()

main()
