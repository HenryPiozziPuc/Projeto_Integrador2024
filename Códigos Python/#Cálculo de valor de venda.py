#Cálculo de valor de venda
CP=float(input("Digite o custo de compra do produto: R$"))
CF=float(input("Digite o custo fixo/administrativo do produto"))
CV=float(input("Digite a comissão de vendas: "))
IV=float(input("Digite o imposto sobre a venda: "))
ML=float(input("Digite a margem de lucro: "))
pv=CP/(1-((CF+CV+IV+ML)/100))
custos=pv*((CF+CV+IV)/100)
rent=((pv-CP-custos)*100/pv)
print(f"O preço de venda do produto é R${pv:.2f}, a rentabilidade é {rent:.2f}% e os custos são de {custos:.2f}")
if rent>=20:
    print("\nO lucro foi alto")
elif 20>rent>=10:
    print("\nO lucro foi médio")
elif 10>rent>=0:
    print("\nO lucro foi baixo")
else:
    print("\nFicou no prejuízo")