barato=0
menor = cont=0
totmil=0
total =0
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont +=1
    total +=preço
    if preço >1000:
        totmil +=1
    if cont==1: #if cont ==1 or preço <menor ---Também pode se escrever desse jeito
        menor= preço
        barato= produto
    else:
        if preço < menor:
            menor = preço
            barato= produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R$ {total:.2f}')
print(f'temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA'))
