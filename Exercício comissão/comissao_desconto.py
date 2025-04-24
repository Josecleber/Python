valor_total = float(input("Digite o valor total da compra: "))

valor_desconto = valor_total * 0.1

valor_parcela = valor_total / 3

comissao_vista = valor_desconto * 0.05

comissao_parcelada = valor_total * 0.05

print("Valor total da compra: R$", valor_total)
print("Valor do desconto: R$", valor_desconto)
print("Valor das parcelas: R$", valor_parcela)
print("Comissão por pagamento à vista: R$", comissao_vista)
print("Comissão por pagamento em 3x: R$", comissao_parcelada)
