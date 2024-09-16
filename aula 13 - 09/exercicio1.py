# Exercício 1
renda = float(input("Digite a sua renda bruta: R$ "))
impostoDevido = 0

if renda > 2000:
    if renda <= 5000:
        impostoDevido = (renda - 2000) * 0.10
    else:
        primeiraFaixaDoImposto = 3000 * 0.10
        segundaFaixaDoImposto = (renda - 5000) * 0.20
        impostoDevido = primeiraFaixaDoImposto + segundaFaixaDoImposto
    
    print(f"Imposto de renda devido: R$ {impostoDevido:.2f} sobre R$ {renda - 2000:.2f}")
else:
    print("Renda isenta de imposto.")