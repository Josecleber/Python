def adicionar_livro(livros, nome, autor, preco, quantidade):
    if nome in livros:
        autor_antigo, preco_antigo, quantidade_antiga = livros[nome]
        nova_quantidade = quantidade_antiga + quantidade
        livros[nome] = (autor_antigo, preco_antigo, nova_quantidade)
    else:
        livros[nome] = (autor, preco, quantidade)

def obter_dados_do_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    preco = float(input("Digite o preço do livro: "))
    quantidade = int(input("Digite a quantidade em estoque do livro: "))
    return nome, autor, preco, quantidade

def listar_livros_por_preco(livros):
    livros_ordenados = [(nome, dados[1]) for nome, dados in livros.items()]
    livros_ordenados.sort(key=lambda x: x[1])
    return livros_ordenados

def sistema_gestao_livraria():
    livros = {}

    while True:
        print("\n Sistema de Gestão da Livraria")
        print("1. Adicionar/Atualizar Livro")
        print("2. Listar Livros por Preço")
        print("3. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            nome, autor, preco, quantidade = obter_dados_do_livro()
            adicionar_livro(livros, nome, autor, preco, quantidade)
            print(f"\n Livro '{nome}' adicionado/atualizado com sucesso!")
            print(f" Estoque atual: {livros}")

        elif opcao == 2:
            livros_ordenados = listar_livros_por_preco(livros)
            print("\n Livros ordenados por preço (crescente):")
            for nome, preco in livros_ordenados:
                print(f"• {nome} - R${preco:.2f}")

        elif opcao == 3:
            print(" Saindo do sistema. Até logo!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

sistema_gestao_livraria()
