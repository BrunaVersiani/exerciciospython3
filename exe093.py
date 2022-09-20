'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo
isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
dados = dict()
partidas = list()
dados['nome'] = str(input('Nome: '))
total_partidas = int(input('Quantas Partidas: '))
for c in range(0, total_partidas):
    partidas.append(int(input(f'    Quantos gols {dados["nome"]} fez na partida {c+1}? ')))
dados['gols'] = partidas[:]
dados['total_gols'] = sum(partidas)
print('*-' * 30)
print(f'    => O(A) jogador(a) {dados["nome"]} jogou {len(dados["gols"])} partidas. ')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i+1} fez {v} gols')
print(f'    => O total de gols é {dados["total_gols"]}. ')
print('*-' * 30)
