##Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. Foram coletados os seguintes dados de cada habitante: 
##idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), cor dos cabelos (L - louros, P - pretos ou C - castanhos).
##Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
##Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos.
##Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes.
##Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) e 
##que tenham olhos azuis e cabelos louros.

idade = []
sexo = []
olhos = []
cabelos = []
def caracteristicas():
    dados = input('Deseja cadastrar outro (S/N)? ')
    while dados == 's' or dados == 'S':
        idade.append(int (input('Digite a idade: ')))
        sexo.append(str (input('Digite o gênero (M ou F): ')))
        olhos.append(str (input('Digite a cor dos olhos (A - azuis ou C - castanhos): ')))
        cabelos.append(str (input('Digite a cor dos cabelos (L - Louros, P - Pretos ou C - Castanhos): ')))
        dados = input('Deseja cadastrar outro (S/N)? ')

def media():
    cont = 0
    soma_idade = 0
    for i in range(len(idade)):
        if (olhos[i] == 'c' or olhos[i] == 'C') and (cabelos[i] == 'p' or cabelos[i] == 'P')):
            cont = cont + 1
            soma_idade = soma_idade + idade[i]
    media_idade = soma_idade / cont
    return media_idade 

def maior():
    for i in range(len(idade)):
        if i == 0:
            maioridade = idade[i]
        if idade[i] >= maioridade:
            maioridade = idade[i]
    return maioridade

def feminino():
    cont = 0
    for i in range(len(sexo)):
        if sexo[i] == 'f' or sexo[i] == 'F':
            if (idade[i] >= 18 and idade[i] <= 35) and (olhos[i] == 'a' or olhos[i] == 'A') and (cabelos[i] == 'l' or cabelos == 'L'):
                cont = cont + 1
    return cont

def main():
    caracteristicas()
    print('A média de idade de pessoas com cabelo preto e olho castanho é',media(),'anos.')
    print('A maior idade é:',maior())
    print('A quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos e que tem olhos azuis e cabelos louros é de:',feminino())

main()
