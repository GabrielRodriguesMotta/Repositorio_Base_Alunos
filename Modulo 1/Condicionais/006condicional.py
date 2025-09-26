#crie um codigo em python que que peça o valor dada conta. se for maior que $100,00,
# adicione uma gorjeta de 10% e exiba o total a pagar.
# caso contrario, adicione uma gorjeta de %5.


valor_conta = float(input("Digite o valor da conta: R$ "))


if valor_conta > 100:
    gorjeta = valor_conta * 500  
else:
    gorjeta = valor_conta * 30


total = valor_conta + gorjeta


print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")

