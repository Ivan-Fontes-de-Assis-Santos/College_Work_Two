import json

def cadastrar_integrantes():
        integrantes = []
        for i in range(4):
            nome = input(f"Digite o nome do integrante {i + 1}: ")
            rm = input(f"Digite o RM do integrante {i + 1}: ")
            integrantes.append({"nome": nome, "rm": rm})
        return integrantes

def cadastrar_produtos():
        produtos = []
        icms_lambda = lambda valor: valor * 0.18

        while True:
            try:
                descricao = input("Digite a descriÃ§Ã£o do produto: ")
                valor = float(input("Digite o valor do produto: "))
                embalagem = input("Digite o tipo de embalagem: ")

                icms = icms_lambda(valor)
                produtos.append({
                    "descricao": descricao,
                    "valor": valor,
                    "embalagem": embalagem,
                    "icms": icms
                })

                continuar = input("Deseja cadastrar um novo produto? (sim/nÃ£o): ").strip().lower()
                if continuar != 'sim':
                    break

            except ValueError:
                print("Erro: Por favor, insira um valor numÃ©rico vÃ¡lido para o preÃ§o do produto.")

        return produtos

def salvar_em_json(integrantes, produtos):
        dados = {
            "integrantes": integrantes,
            "produtos": produtos
        }
        with open('1_5_arquivo_produto.json', 'w') as json_file:
            json.dump(dados, json_file, indent=4)

def main():
        print("Cadastro de Integrantes")
        integrantes = cadastrar_integrantes()

        print("\nCadastro de Produtos")
        produtos = cadastrar_produtos()

        if len(produtos) >= 5:
            salvar_em_json(integrantes, produtos)
            print("Cadastro concluÃ­do e salvo em 1_5_arquivo_produto.json")
        else:
            print("Ã‰ necessÃ¡rio cadastrar pelo menos 5 produtos.")

if __name__ == "__main__":
        main()
