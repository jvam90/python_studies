print("Seja bem vindo e experimente a linguica!\n**********")
produto = input("Qual o produto voce quer comprar: ")
preco = float(input("Qual o preco do produto: "))
quantidade = int(input("Quantos itens: "))

print(f"Adicionados {quantidade} {produto} ao carrinho.")
print(f"Subtotal: {float(preco * quantidade)}")
