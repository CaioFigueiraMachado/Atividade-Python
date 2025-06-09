#Caio Figueira Machado 2BDEV
produtos = []


def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    
    produtos.append(produto)
    print(f"\nProduto '{nome}' adicionado com sucesso!")


def buscar_produto():
    nome_busca = input("Digite o nome do produto que deseja buscar: ")
    encontrado = False

    for produto in produtos:
        if produto['nome'].lower() == nome_busca.lower():
            print("\nProduto encontrado:")
            print(f"  Nome: {produto['nome']}")
            print(f"  Preço: R$ {produto['preco']:.2f}")
            print(f"  Quantidade em estoque: {produto['quantidade']}")
            encontrado = True
            break

    if not encontrado:
        print(f"\nProduto '{nome_busca}' não encontrado.")


def listar_produtos():
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    print("\nLista de Produtos:")
    for produto in produtos:
        print(f"  Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Estoque: {produto['quantidade']}")


def atualizar_estoque():
    nome_busca = input("Digite o nome do produto que deseja atualizar: ")
    for produto in produtos:
        if produto['nome'].lower() == nome_busca.lower():
            nova_quantidade = int(input(f"Digite a nova quantidade para '{produto['nome']}': "))
            produto['quantidade'] = nova_quantidade
            print(f"\nEstoque do produto '{produto['nome']}' atualizado com sucesso.")
            return
    print(f"\nProduto '{nome_busca}' não encontrado.")


while True:
    print("\n=== Menu de Controle de Estoque ===")
    print("1. Adicionar produto")
    print("2. Buscar produto")
    print("3. Listar todos os produtos")
    print("4. Atualizar estoque de produto")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        buscar_produto()
    elif escolha == '3':
        listar_produtos()
    elif escolha == '4':
        atualizar_estoque()
    elif escolha == '5':
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
