# Solicite ao usuário 4 notas.
# Calcule a média
# Informe se o aluno está aprovado (media>=7), recuperação(5<media<7) ou reprovado.
# Apresente as notas que o aluno tirou, a media e o status de sua situação


# lista
# for
#if, elif, else

notas = []

for i in range(4):
    nota = float(input(f'Informe a nota da prova {i+1}: '))
    if nota > 0:
        notas.append(nota)
    else:
        print('Valor inválido.')
print(f'Suas notas são: {notas}')  # linha opcional
media = sum(notas)/len(notas)

if media >=7:
    print(f'Suas notas foram{notas}, sua {media:.2f} e você está aprovado. ')
elif 5 <= media < 7:
    print(f'Suas notas foram{notas}, sua {media:.2f} e você está de recuperação. ')
else:
    print(f'Suas notas foram{notas}, sua {media:.2f} e você está reprovado. ')