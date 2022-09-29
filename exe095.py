#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
time = list()
dados = dict()
partidas = list()

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    total_partidas = int(input('Quantas Partidas: '))
    partidas.clear()
    for c in range(0, total_partidas):
        partidas.append(int(input(f'    Quantos gols {dados["nome"]} fez na partida {c+1}? ')))
    dados['gols'] = partidas[:]
    dados['total_gols'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resposta = str(input('Deseja incluir mais jogadores? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print('*-' * 30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-~' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar!) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Erro! Não tem dados registrados com este {busca} de codigo!')
    else:
        print(f'---> Levantamento do(a) Jogador(a) {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-~' * 30)
print(f'{"<<<Volte sempre!>>>":^60}')
print('*-' * 30)

