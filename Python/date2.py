def gera_nome_convite(nome_convidado):
    posicao_final = len(nome_convidado)
    posicao_inicial = posicao_final - 4
    parte1 = nome_convidado[0:4]
    parte2 = nome_convidado[posicao_final-4:posicao_final]
    print ('%s %s' %(parte1, parte2))