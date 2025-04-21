#Como hacer tablas de verdad

print('')
print('Tabla de verdad con OR') #Tabla del OR
print('')
print('P\t Q\t P OR Q')
booleanos = [True,False]
for x in booleanos:
    for y in booleanos:
        print('{}\t{}\t{}'.format(x,y, x and y))

print('')
print('Tabla de verdad con AND')    #Tabla del AND
print('')

print('P\t Q\t P Y Q')
booleanos = [True,False]
for x in booleanos:
    for y in booleanos:
        print('{}\t{}\t{}'.format(x,y, x and y))

print('')
print('Tabla de verdad con NOT')    #Tabla del NOT
print('')

print('P\t ~P')
booleanos = [True,False]
for x in booleanos:
    print('{}\t{}'.format(x, not x))