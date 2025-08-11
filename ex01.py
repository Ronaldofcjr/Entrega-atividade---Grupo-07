tipo = input("A ou G?")
litros = float(input("Quantidade Litros?"))

if tipo == 'A':
    if litros <= 20:
        valor = (litros * 1.90)*0.97

    else:
        valor = (litros * 1.90)*0.95
    

elif tipo == 'G':
    if litros <= 20:
        valor = (litros * 2.50)*0.96

    else:
        valor = (litros * 2.50)*0.94

else:
    print("Ops, não encontrado")

print(f'{valor:.2f}')