print('Bem-vindo a pizarria kalash.')

size = input('Qual tamanho você gostria de pedir, Pequena(p) Media(m) grande(l) ')

if size == 'p':
    custo = 15
    peperone = input('Gostaria de peperone? sim(s) não(n) ')
    queijo = input('Gostaria de queijo? sim(s) não(n) ')
    refrigerante = input('Gostaria de refrigerante também?, sim(s) não(n)')

    if peperone == 's':
        custo += 2
    if queijo == 's':
        custo += 1
    if refrigerante == 's':
        custo += 5

    print(f'Sua pizza vai custar R${custo:.2f}')

elif size == 'm':
    custo = 20
    peperone = input('Gostaria de peperone? sim(s) não(n) ')
    queijo = input('Gostaria de queijo? sim(s) não(n) ')
    refrigerante = input('Gostaria de refrigerante também?, sim(s) não(n)')

    if peperone == 's':
        custo += 3
    if queijo == 's':
        custo += 1
    if refrigerante == 's':
        custo += 5

    print(f'Sua pizza vai custar R${custo:.2f}')

else:
    custo = 25
    peperone = input('Gostaria de peperone? sim(s) não(n) ')
    queijo = input('Gostaria de queijo? sim(s) não(n) ')
    refrigerante = input('Gostaria de refrigerante também?, sim(s) não(n)')

    if peperone == 's':
        custo += 3
    if queijo == 's':
        custo += 1
    if refrigerante == 's':
        custo += 5

    print(f'Sua pizza vai custar R${custo:.2f}')