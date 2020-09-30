
print('''Digite 1 para converter um número inteiro para BINARIO
Digite 2 para converter binário para INTEIRO''')

opcao=int(input("Qual a opção desejada? ")) #lê a opção desejada

while (opcao <1 or opcao>2): #enquanto o numero digitado for diferente do menu, vai executar esse comando
    opcao=int(input('Opção inválida, tente novamente!')) #lê o numero novamente

if opcao==1:
    valor = int(input('Digite um número inteiro : ')) #entrada do numero inteiro

    '''
    usando o .format podemos puxar o conversor do python
    e usando a função [2:] podemos pular as 2 primeiras casas que sao irrelevantes (nesse caso)
    usamos o {} para mostrar os resultados recebidos OBS: VAI IR EM ORDEM
    '''

    print("O número {} convertido para BINÁRIO é {}".format(valor, bin(valor)[2:]))


elif opcao==2:
    valor = int(input('Digite o número binário: ')) #entrada do binario
    otvalor= int(str(valor), 2) #variavel vai converter o valor binario para decimal, pq utilizamos o numero 2
    print("O binário ", valor, "convertido para DECIMAL é", otvalor)


