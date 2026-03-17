def funcao_teste():
    # Leitura da linha de identificadores de transações
    entrada = input().split() # separei os valores do usuário, criando uma lista
    transacoes_unicas = [] #criei uma lista vazia

    #com o input do usuario separado, eu fico verificando se o input do usuario está na lista vazia (transacoes_unicas)
    for lista in entrada: 
        if lista not in transacoes_unicas: #se a lista (que é o input do usuario já separado) não estiver dentro da nova lista (resultado)
            transacoes_unicas.append(lista) #adicionamos o item da lista no resultado

    print(' '.join(transacoes_unicas))  # Descomente após implementar a lógica

funcao_teste()
#print(*resultado)
# TODO: Crie uma lista com as transações sem duplicatas, mantendo a ordem da primeira ocorrência

# Dica: Percorra cada transação e adicione à lista apenas se ainda não estiver presente
