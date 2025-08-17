import requests


def buscar_pais(nome):


    url = f'https://restcountries.com/v3.1/name/{nome}'

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao buscar informações do país.")
        return
    
    dados = response.json()[0]  

    
    nome = dados.get("name", {}).get("common", "N/A")
    linguas = list(dados.get("languages", {}).values())
    regiao = dados.get("region", "N/A")
    subregiao = dados.get("subregion", "N/A")
    capital = dados.get("capital", ["N/A"])[0]

    
    moedas = dados.get("currencies", {})
    for sigla, info in moedas.items():
        moeda_sigla = sigla
        moeda_nome = info.get("name", "N/A")
        moeda_simbolo = info.get("symbol", "N/A")

    
    fronteiras = dados.get("borders", [])

    
    print(f" País: {nome}")
    print(f" Línguas: {', '.join(linguas)}")
    print(f" Região: {regiao} / {subregiao}")
    print(f" Capital: {capital}")
    print(f" Moeda: {moeda_sigla} - {moeda_nome} ({moeda_simbolo})")
    print(f" Fronteiras: {', '.join(fronteiras) if fronteiras else 'Nenhuma'}")

pais = input("Digite o nome do País: ")

buscar_pais(pais)


