'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
 em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
 C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média'''
pessoas = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(('ERRO! Por favor, digite apenas M ou F.'))
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print(('ERRO! Por favor, digite apenas S ou N.'))
    if resposta == 'N':
        break
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'A média das idades é {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end='')
    print()
print(f'A lista de pessoas que estão com a idade acima da media:')
for p in pessoas:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f"{k} = {v} ;", end='')
        print()
print('--- Encerrado! ---')
