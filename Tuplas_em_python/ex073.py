'''.73 Crie um programa preenchida com os 20 primeiros colocados na tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a, Apenas os 5 primeiros colocados
b, Os últimos 4 colocados
c, Uma lista com os times em ordem alfabética
d, Em que posição na tabela está o time da Chapecoense:'''

tabela =('Corinthians','Palmeiras','São Paulo','Cruzeiro','Fluminense','Atletico Paranaese','Bahia','Coritiba','Internacional','Grêmio','Ceará','Atletico-MG','Vitória','Chapecoense','Botafogo','Santos','Sport','Vasco da Gama','Ponte Preta','Nautico')
print('=-'*30)
print(f'\033[1;32mOs cinco primeiros colocados são:\n{tabela[:5]}\033[m')
print('=-'*30)
print(f'\033[1;31mOs quatro últimos colocados são:\n{tabela[-4:]}\033[m')
print('=-'*30)
print(f'A tabela em ordem alfabética é:\n',sorted(tabela))
print('=-'*30)
print(f'\033[1;35mO time da Chapecoense está na {tabela.index("Chapecoense")}° posição\033[m')


