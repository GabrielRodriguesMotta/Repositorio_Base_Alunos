# Crie um programa que some todos os números ímpares
# que são multiplos de 3 e 1 a 30 e apresente o resultado.

# Etapas para resolução
# 1) criar um for para captar os números impares
# 2) criar uma condicional para checar se o número é multiplo de 3
# 3) somar os numeros que atende a condicional
# 4) apresentar os resultados
multiplo_tres = 0 # variavel que irá receber os números impares e multiplos de 3

for i in range(1,31,2): # contagem dos números impares
    if i % 3 == 0: #checagem se os números são multiplos
        print(i, end=',') # apresentação dos números que atendem os requisitos
        #(na mesma linha, separados por vírgula)
        multiplo_tres += i
print() # pular uma linha
print(f'A soma dos números impares multiplos de 3 neste intervalo é {multiplo_tres}.')

