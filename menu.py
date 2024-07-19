import requests
import matplotlib.pyplot as plt

def exibir_menu():
    print("\n" + "="*40)
    print("{:^40}".format("MENU PRINCIPAL"))
    print("="*40)
    print("1. Listar livros")
    print("2. Adicionar livro")
    print("3. Atualizar livro")
    print("4. Remover livro")
    print("5. Agrupar por gênero")
    print("6. Sair")
    print("="*40)

def listar_livros():
    url = "http://localhost:3000/livros"
    response = requests.get(url)
    if response.status_code == 200:
        livros = response.json()
        print("\n" + "-"*40)
        print("{:^40}".format("LISTA DE LIVROS"))
        print("-"*40)
        for livro in livros:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Preço: R${livro['preco']:.2f}")
        print("-"*40)
    else:
        print("Erro ao obter a lista de livros.")

def adicionar_livro():
    titulo = input("\nDigite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    preco = float(input("Digite o preço do livro: "))

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "preco": preco
    }

    url = "http://localhost:3000/livros"
    response = requests.post(url, json=novo_livro)
    if response.status_code == 201:
        print("Livro adicionado com sucesso!")
    else:
        print("Erro ao adicionar o livro.")

def atualizar_livro():
    livro_id = int(input("\nDigite o ID do livro a ser atualizado: "))
    novo_preco = float(input("Digite o novo preço do livro: "))

    url = f"http://localhost:3000/livros/{livro_id}"
    response = requests.put(url, json={"preco": novo_preco})
    if response.status_code == 200:
        print("Livro atualizado com sucesso!")
    else:
        print("Erro ao atualizar o livro.")

def remover_livro():
    livro_id = int(input("\nDigite o ID do livro a ser removido: "))

    url = f"http://localhost:3000/livros/{livro_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Livro removido com sucesso!")
    else:
        print("Erro ao remover o livro.")

def agrupar_por_genero():
    url = "http://localhost:3000/livros"
    response = requests.get(url)
    if response.status_code == 200:
        livros = response.json()
        generos = {}

        for livro in livros:
            genero = livro["genero"]
            generos.setdefault(genero, 0)
            generos[genero] += 1

        print("\n" + "-"*40)
        print("{:^40}".format("LIVROS POR GÊNERO"))
        print("-"*40)
        for genero, quantidade in generos.items():
            print(f"Gênero: {genero}, Quantidade: {quantidade}")
        print("-"*40)

        # Criar um gráfico de barras
        plt.bar(generos.keys(), generos.values())
        plt.xlabel("Gênero")
        plt.ylabel("Quantidade")
        plt.title("Quantidade de Livros por Gênero")
        plt.show()
    else:
        print("Erro ao obter a lista de livros.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            remover_livro()
        elif opcao == "5":
            agrupar_por_genero()
        elif opcao == "6":
            print("Encerrando a aplicação.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
