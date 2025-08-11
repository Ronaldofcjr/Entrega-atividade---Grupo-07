valor_saque = int(input('valor?'))
valor_aux = valor_saque

nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = 0

while valor_saque > 0:
    while valor_saque - 100 >= 0:
        nota_100 += 1
        valor_saque -= 100

    while valor_saque - 50 >= 0:
        nota_50 += 1
        valor_saque -= 50

    while valor_saque - 10 >= 0:
        nota_10 += 1
        valor_saque -= 10

    while valor_saque - 5 >= 0:
        nota_5 += 1
        valor_saque -= 5

    while valor_saque - 1 >= 0:
        nota_1 += 1
        valor_saque -= 1
    
print(f'Notas 100:{nota_100} - Notas 50:{nota_50} - Notas 10:{nota_10} - Notas 5:{nota_5} - Notas 1:{nota_1}')

    

    
