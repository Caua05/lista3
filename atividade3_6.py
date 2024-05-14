listas = ['Neymar','Messi','Cristiano Ronaldo', 'Vini jr', 'Gabigol']
for lista in listas:
    print('Você foi convidado para a festa do cauã', lista)
nome_removido = 'Messi'
if nome_removido in listas:
    listas.remove(nome_removido)
    print(f'O  {nome_removido}','Não vai comparecer para o jantar')
novas = ['Neymar','Ribamar','Cristiano Ronaldo', 'Vini jr', 'Gabigol']    
for nova in novas:
    print('Você foi convidado para a festa do cauã', nova)
    