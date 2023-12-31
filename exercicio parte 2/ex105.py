def notas(*n, sit= False): # Returnar dicionarios
    '''
     -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: Valor opcional, indicando se deve ou não aceitar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if  sit:
        if r['média'] >=7:
            r['situação'] = 'BOA'
        elif r['média'] >=5:
            r['situação']= 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r
resp = notas(5, 5, 2, 5, sit=True)
print(resp)
