import os
from prettytable import PrettyTable
# Definição da função para cadastrar um novo produto
def cadastrar_produto():
    os.system("cls")  # Limpa a tela do console (apenas Windows)
    table = PrettyTable()

    print(f"\n\tCadastro de produto!")  # Mensagem de cabeçalho para o cadastro

    # Solicita e armazena os dados do produto inseridos pelo usuário
    global cod_prod
    cod_prod = int(input("Código do produto: "))
    table.add_column(f"Código do Produto",[cod_prod])

    global nome_prod
    nome_prod = input("Nome do produto: ")
    table.add_column(f"Nome",[nome_prod])

    global desc_prod
    desc_prod = input("Descrição: ")
    table.add_column(f"Descrição",[desc_prod])

    global custo_prod
    custo_prod = float(input("Custo de compra: R$ "))
    table.add_column(f"Custo de Compra",[custo_prod])

    global custo_fixo_prod
    custo_fixo_prod = float(input("Custo fixo/administrativo [%]: "))
    table.add_column(f"Custo Fixo/Administrativo",[custo_fixo_prod])

    global comissao_vendas
    comissao_vendas = float(input("Comissão de vendas [%]: "))
    table.add_column(f"Comissão de vendas",[comissao_vendas])

    global imposto_prod
    imposto_prod = float(input("Imposto sobre a venda [%]: "))
    table.add_column(f"Imposto sobre a venda",[imposto_prod])

    global lucro_prod
    lucro_prod = float(input("Margem de lucro [%]: "))
    table.add_column(f"Imposto sobre a venda",[lucro_prod])
    # Retorna os dados do produto
    print(f"\n{table}")
    calculo_preco()
    
# Definição da função para calcular o preço de venda, custos e rentabilidade do produto
def calculo_preco():
    # Cálculo do preço de venda
    preco_venda = (custo_prod) / (1 - ((custo_fixo_prod + comissao_vendas + imposto_prod + lucro_prod) / 100))
    # Cálculo dos custos
    custos = preco_venda * ((custo_fixo_prod + comissao_vendas + imposto_prod) / 100)
    # Cálculo da rentabilidade
    rentabilidade = ((preco_venda / custo_prod) - 1) * 100
    # Exibição dos resultados
    print(f"O preço de venda do produto é R${preco_venda:.2f}, o lucro bruto é {rentabilidade:.2f}% e os custos são de {custos:.2f}")
    # Verifica a rentabilidade e exibe uma mensagem correspondente
    if rentabilidade >= 20:
        print("\nO lucro foi alto")
    elif 20 > rentabilidade >= 10:
        print("\nO lucro foi médio")
    elif 10 > rentabilidade >= 0:
        print("\nO lucro foi baixo")
    else:
        print("\nFicou no prejuízo")
    # Retorna o preço de venda, custos e rentabilidade
    return preco_venda, custos, rentabilidade

# Função principal
def main():
    # Exibe o menu e solicita a escolha do usuário
    escolha = int(input(f"\t     MENU\n\t| 1- Cadastrar |\n\t| 2- Listar    |\n\t| 3- Alterar   |\n\t| 4- Excluir   |\n\t| 5- Sair      |\nO que deseja fazer? "))
    # Verifica a escolha do usuário
    match escolha:
        # Caso a escolha seja 1 (Cadastrar)
        case 1:
            cadastrar_produto()  # Chama a função para cadastrar um produto
        # Caso a escolha seja 2 (Listar)
        case 2:
            listagem_de_dados()  # Chama a função para listar dados (não definida no código fornecido)
        # Caso a escolha seja 3 (Alterar)
        case 3:
            alteracao_de_dados()  # Chama a função para alterar dados (não definida no código fornecido)
        # Caso a escolha seja 4 (Excluir)
        case 4:
            exclusao_de_dados()  # Chama a função para excluir dados (não definida no código fornecido)
        # Caso a escolha seja 5 (Sair)
        case 5:
            print(f"Até mais!")  # Exibe mensagem de despedida
            exit()  # Encerra o programa
        # Caso a escolha não seja válida
        case default:
            print("Digite uma opção válida")  # Exibe uma mensagem indicando uma escolha inválida
            main()  # Chama novamente a função principal para que o usuário faça uma nova escolha

# Chamada da função principal
main()
