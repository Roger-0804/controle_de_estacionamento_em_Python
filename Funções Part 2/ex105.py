'''105. Faça um programa que tenha uma função chamada notas( ) que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
A ) A maoir nota
B ) A menor nota
C ) A média da turma
D ) A situação (Opcional)'''


def notas(*n,sit=False):
    """
    => Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional.indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação dos alunos
    """
    r ={}
    r['total']=len(n)
    r['Maior']=max(n)
    r['Menor']=min(n)
    r['Media']=sum(n)/len(n)
    if sit:
        if r['Media'] >=7:
            r['Situação'] = 'Boa '
        elif r['Media'] >=5:
            r['Situação'] ='Razoável'
        else:
            r['Situação'] ='Ruim'
    return r


resp = notas(5,3,1.5,sit=True)
'help(notas)'
print(resp)