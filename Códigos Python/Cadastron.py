
#obtenção de dados  
Cod_prod = int(input("Digite o codigo do produto:\n"))
nome_prod = input("Digite o nome do produto:\n")
desc_prod = input("Digite a discrição do produto:\n")
custo_prod = float(input("Digite o custo de compra do produto:\n R$"))
custo_fixo_prod = float(input("Digite o custo fixo/administrativo do produto:\n "))
comissao_vendas = float(input("Digite a comissão de vendas:\n "))
imposto_prod =float(input("Digite o imposto sobre a venda:\n "))
lucro_prod =float(input("Digite a margem de lucro:\n "))

def calculo_preco(custo_prod, custo_fixo_prod, comissao_vendas, imposto_prod, lucro_prod):
    preco_venda = (custo_prod)/(1-((custo_fixo_prod + comissao_vendas + imposto_prod + lucro_prod)/100))
    custos = preco_venda*((custo_fixo_prod+comissao_vendas+imposto_prod)/100)
    rentabilidade = ((preco_venda/custo_prod) - 1)*100
    return preco_venda, custos, rentabilidade

def main(custo_prod, custo_fixo_prod, comissao_vendas, imposto_prod, lucro_prod):
    preco_venda, custos, rentabilidade = calculo_preco(custo_prod, custo_fixo_prod, comissao_vendas, imposto_prod, lucro_prod)
    print(f"O preço de venda do produto é R${preco_venda:.2f}, o lucro bruto é {rentabilidade:.2f}% e os custos são de {custos:.2f}")
    if rentabilidade>=20:
        print("\nO lucro foi alto")
    elif 20>rentabilidade>=10:
        print("\nO lucro foi médio")
    elif 10>rentabilidade>=0:
        print("\nO lucro foi baixo")
    else:
        print("\nFicou no prejuízo")


main(custo_prod, custo_fixo_prod, comissao_vendas, imposto_prod, lucro_prod)