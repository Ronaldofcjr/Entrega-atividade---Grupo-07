import requests

moedas = {
"USD": "dólares americanos",
"EUR": "euros",
"GBP": "libras esterlinas",
"JPY": "ienes japoneses",
"ARS": "pesos argentinos",
"CNY": "yuans chineses",
"CAD": "dólares canadenses",
"AUD": "dólares australianos"
 }

    

moeda = input("Digite a sigla da moeda (ex: USD, EUR, GBP): ")
valor = float(input("Digite o valor em reais: "))

url = 'https://api.exchangerate-api.com/v4/latest/BRL'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    if moeda in dados["rates"]:
        cotacao = dados["rates"][moeda]

        nome_moeda = moedas.get(moeda, moeda)
        valor_convertido = valor * cotacao
        print(f"O valor convertido é R$ {valor_convertido:.2f} {nome_moeda}")
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao buscar a cotação da moeda.")
        



