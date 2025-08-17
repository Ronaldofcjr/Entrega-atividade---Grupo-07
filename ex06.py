salario = 1000.00

ano_contratacao = 1995
ano_atual = 2025

percentual_aumento = 0.015

for ano in range(ano_contratacao +1, ano_atual +1):
    salario += salario *percentual_aumento
    percentual_aumento *= 2

print(f"Salário atual do funcionário em {ano_atual} é de R$ {salario:.2f}")


while True:
    salario = float(input("Digite o salario inicial: "))

    ano_contratacao = 1995
    ano_atual = 2025

    percentual_aumento = 0.015

    for ano in range(ano_contratacao +1, ano_atual +1):
        salario += salario *percentual_aumento
        percentual_aumento *= 2

    print(f"Salário atual do funcionário em {ano_atual} é de R$ {salario:.2f}") 

    break