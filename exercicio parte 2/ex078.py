maior = menor=0
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c} ')))
    if  c==0:
        maior=menor=listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
                menor= listanum[c]
print('=-'*22)
print(f'Voçê digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posiçõs ', end='')
for i, v in enumerate(listanum):
    if v ==maior:
        print(f'{i}...', end='')

print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i,v in enumerate(listanum):
    if v ==menor:
        print(f'{i}...')
print()
