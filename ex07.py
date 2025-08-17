valores = []


while True:
    n = int(input("Informe um numero: "))
    if n == -1:
        break
    valores.append(n)





lidos = len(valores)
print(f'Foram inputador: {lidos} numeros')

print("Valores na ordem informada:", valores)

print("Valores na ordem inversa:", valores[::-1])


soma = sum(valores)

print(f"Soma de todos os valores da lista {soma}")

media = soma / lidos

print(f"Media dos valores: {media}")

acima_media = sum(1 for v in valores if v > media)
print(f"Quantidade de valores acima da média: {acima_media}")

