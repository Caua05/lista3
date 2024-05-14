x=int(input('Digite um numero: '))
y=int(input('Digite outro numero: '))
soma = x + y

for count in range(10):
    print('%d x %d = %d' % (soma, count + 1, soma*(count + 1)))