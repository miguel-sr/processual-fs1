# Exercício 2
def calcularTotalComDesconto(totalCompra):
    desconto = 0
    if totalCompra > 100:
        desconto = 0.10
    elif totalCompra > 50:
        desconto = 0.05
    
    valorDesconto = totalCompra * desconto
    totalFinal = totalCompra - valorDesconto
    
    return valorDesconto, totalFinal

def main():
    itens = input("Digite os valores dos itens, separados por espaço: ")
    listaItens = itens.split()
    totalCompra = sum(float(valor) for valor in listaItens)
    
    if totalCompra < 0:
        print("O total da compra não pode ser negativo.")
        return
    
    valorDesconto, totalFinal = calcularTotalComDesconto(totalCompra)
    
    print(f"Valor total da compra: R$ {totalCompra:.2f}")
    print(f"Desconto aplicado: R$ {valorDesconto:.2f}")
    print(f"Valor final após desconto: R$ {totalFinal:.2f}")

main()
