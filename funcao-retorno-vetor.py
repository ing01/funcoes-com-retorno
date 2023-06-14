# Algoritmo com função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, que armazenará o fatorial de cada elemento de A. 
# Retorne/apresente o vetor B.

def fatorial():
  vetorA = []
  vetorB = []
  for n in range(5):
    vetorA.append(int(input('Digite um valor: ')))
    resultado = 1
    for i in range(1, vetorA[n]+1):
      resultado = resultado * i
    vetorB.append(resultado)
  return vetorB

def main():
  f = fatorial()
  print('O fatorial dos valores digitados são', f)

main()
