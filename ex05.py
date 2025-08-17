cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00),
    }

print("=== CARDÁPIO ===")
for codigo, (produto, preco) in cardapio.items():
    print(f"{codigo} - {produto} - R$ {preco:.2f}")

total_geral = 0

while True:
    codigo = int(input("\nDigite o código do produto (ou 0 para encerrar): "))

    if codigo == 0:  
         break

    if codigo not in cardapio:
        print("Código inválido! Tente novamente.")
        continue

    quantidade = int(input(f"Quantos '{cardapio[codigo][0]}' deseja? "))

    nome, preco = cardapio[codigo]
    valor_item = preco * quantidade
    total_geral += valor_item

    print(f"{quantidade} x {nome} = R$ {valor_item:.2f}")

print("\n=== RESUMO DO PEDIDO ===")
print(f"Total a pagar: R$ {total_geral:.2f}")