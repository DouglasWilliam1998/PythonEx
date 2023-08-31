produtos=-1
somadosProdutos=0
numerodeProdutos=1
while produtos!=0:
    produtos=float(input())
    if produtos==0:
        break
    print(f"Produto {numerodeProdutos} : R$ {produtos} ")
    somadosProdutos+=produtos
    numerodeProdutos+=1
valorPago=float(input())
print(f"Valor Pago: R$ {valorPago}")
troco=(valorPago-somadosProdutos)
print(f"Troco: R$ {troco}")