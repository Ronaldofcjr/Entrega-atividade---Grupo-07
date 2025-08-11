nota_1 = float(input("Nota 1 ?"))
nota_2 = float(input("Nota 2 ?"))
media = ((nota_1 + nota_2) / 2)
situacao = ""

if media >= 9:
    conceito = 'A'
    situacao = "Aprovado"

elif media >= 7.5:
    conceito = 'B'
    situacao = "Aprovado"

elif media >= 6:
    conceito = 'C'
    situacao = "Aprovado"

elif media >= 4:
    conceito = 'D'
    situacao = "Reprovado"

elif media >= 0:
    conceito = 'E'
    situacao = "Reprovado"

else:
    print("Não encontrado")