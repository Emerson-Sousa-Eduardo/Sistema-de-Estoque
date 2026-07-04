# Sistema de Estoque com Python
# Este é um sistema simples de gerenciamento de estoque implementado em Python. Ele permite cadastrar produtos, listar produtos, buscar produtos, atualizar a quantidade de produtos e remover produtos do estoque.
# foram usadas funções para organizar o código e facilitar a manutenção. O sistema utiliza um arquivo de texto para armazenar os dados dos produtos.

#                          Funções do Sistema de Estoque

# Função para cadastrar um novo produto no estoque
def cadastrar_produto():
        print("Cadastrar Produto")

        nome_produto = input("Digite o nome do produto: ")
        try:
            quantidade_produto = int(input("Digite a quantidade do produto: "))
        except ValueError:
            print("Certifique-se de digitar apenas números inteiros!")
            return
        try:
            preco_produto = float(input("Digite o preço do produto: "))
        except ValueError:
            print("Certifique-se de digitar apenas números decimais!")
            return
        with open("estoque.txt", "a") as arquivo:
            arquivo.write(f"{nome_produto},{quantidade_produto},{preco_produto}\n")
        print("Produto cadastrado com sucesso!")

# Função para listar todos os produtos cadastrados no estoque
def listar_produtos():
        print("Listar Produtos")
        try:
            with open("estoque.txt", "r") as arquivo:
                produtos = arquivo.readlines()
            if len(produtos) == 0:
                print("Nenhum produto cadastrado.")
            else:
                for produto in produtos:
                    nome, quantidade, preco = produto.strip().split(",")
                    print("-" * 30)
                    print(f"Nome: {nome}")
                    print(f"Quantidade: {quantidade}")
                    print(f"Preço: R$ {preco}")
        except FileNotFoundError:
            print("Nenhum produto cadastrado.")
            return

# função para buscar um produto no estoque    
def buscar_produto():
        print("Buscar Produto")
        
        nome_produto = input("Digite o nome do produto: ")
        try:
            with open("estoque.txt", "r") as arquivo:
                produtos = arquivo.readlines()
            encontrado = False
            for produto in produtos:
                nome, quantidade, preco = produto.strip().split(",")
                if nome == nome_produto:
                    print("-" * 30)
                    print(f"Nome: {nome}")
                    print(f"Quantidade: {quantidade}")
                    print(f"Preço: R$ {preco}")
                    encontrado = True
                    break
            if not encontrado:
                print("Produto não encontrado.")
        except FileNotFoundError:
            print("Nenhum produto cadastrado.")
   
# função para atualizar a quantidade de um produto no estoque   
def atualizar_quantidade():
        print("Atualizar quantidade")
        
        nome_produto = input("Digite o nome do produto: ")
        try:
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
        except ValueError:
            print("Certifique-se de digitar apenas números inteiros!")
            return
        print(f"Quantidade do produto {nome_produto} atualizada para {nova_quantidade}.")

# função para remover um produto do estoque
def remover_produto():
        print("Remover Produto")
        
        nome_produto = input("Digite o nome do produto: ")
        resposta = input(f"Tem certeza que deseja remover o produto {nome_produto}? (s/n): ")
        if resposta.lower() == "s":
            print(f"Produto {nome_produto} removido do estoque.")
            return
        elif resposta.lower() != "s" and resposta.lower() != "n":
            print("Opção inválida. Selecione apenas (s/n).")
        else:    
            print("Operação cancelada.")
            return
    

print("=" * 35)
print("Bem-vindo ao Sistema de Estoque!")
print("=" * 35)

# loop do menu principal do sistema
while True:
    print("\nMenu Principal")
    print("=" * 15)
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Buscar Produto")
    print("4. Atualizar Quantidade")
    print("5. Remover Produto")
    print("0. Sair")

    # Solicita ao usuário que escolha uma opção do menu e trata possíveis erros de entrada
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Certifique-se de digitar apenas números!")
        continue
    
    # Executa a função correspondente à opção escolhida pelo usuário
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        buscar_produto()
    elif opcao == 4:
        atualizar_quantidade()
    elif opcao == 5:
        remover_produto()
    elif opcao == 0:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Escolha uma opção do menu.")