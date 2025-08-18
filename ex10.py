import requests

zonas_sp = {
    "Zona Norte": ["Santana", "Casa Verde", "Vila Maria", "Tucuruvi", "Jaçanã", "Mandaqui", "Vila Medeiros"],
    "Zona Sul": ["Santo Amaro", "Capão Redondo", "Campo Limpo", "Jabaquara", "Morumbi", "Socorro"],
    "Zona Leste": ["Itaquera", "São Mateus", "Penha", "Tatuapé", "Aricanduva", "Guaianases"],
    "Zona Oeste": ["Lapa", "Butantã", "Pinheiros", "Perdizes", "Jaguaré", "Raposo Tavares"],
    "Centro": ["Sé", "Bela Vista", "Liberdade", "Santa Cecília", "Consolação", "Bom Retiro"]
}

cep = input("Digite o CEP de destino: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)

if response.status_code == 200:
    dados = response.json()

    if "erro" in dados:
        print("CEP inválido.")
    else:
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "")
        uf = dados.get("uf", "")

        if cidade.lower() == "são paulo":
            zona_encontrada = None
            for zona, bairros in zonas_sp.items():
                if any(bairro.startswith(b) for b in bairros):
                    zona_encontrada = zona
                    break

            if zona_encontrada:
                print(f"Bairro: {bairro}, {zona_encontrada} de São Paulo.")
            else:
                print(f"Bairro: {bairro}, região não classificada.")
        else:
            print(f"Cidade: {cidade}/{uf} (fora da Grande São Paulo).")
else:
    print("Erro ao acessar a API do ViaCEP.")
