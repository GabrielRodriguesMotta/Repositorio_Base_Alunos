# Crie um programa  que leia o peso de 5 pessoas.
# no final, mostre qual foi o maior e o menor peso lido


# etapas para resolução:
# 1) crie uma lista vazia para receber os pesos
# 2) crie um FOR para receber os pesos das 5 pessoas.
# 3) adicione os pesos das 5 pessoas
# 4) utilize a função max() e min() ou ordene a lista e busque o primeiro e o último elemento
# 5) apresente os resultados

pesos = []

for i in range(5):
    peso = float(input('Informe seu peso em Kg: '))
    pesos.append(peso)
print(f'A lista dos pesos em Kg: ')

# maior_peso = max(pesos)
# menor_peso = min(pesos)
# print(f'O maior peso é {maior_peso} Kg e o menor peso é {menor_peso} Kg.')

# outra maneira de resolver o maior e o menor
pesos.sort()
menor = pesos[0]
maior = pesos[-1]
print(f'O maior peso é {maior} Kg e o menor peso é {menor} Kg.')