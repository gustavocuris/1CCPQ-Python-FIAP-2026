# SISTEMA DE NOTA PONDERADA FIAP
n1 = float(input('  * DIGITE NOTA DO 1° TRIMESTE: ').replace(',', '.'))
n2 = float(input(' \n * DIGITE NOTA DO 2° TRIMESTE: ').replace(',', '.'))
n3 = float(input(' \n * DIGITE NOTA DO 3° TRIMESTE: ').replace(',', '.'))
n4 = float(input(' \n * DIGITE NOTA DO 4° TRIMESTE: ').replace(',', '.'))

# CALCULO DAS MÉDIAS
vnotas = n1 + n2 + n3 + n4

vtotal = vnotas / 4

# PRINTS
print(f" \n * SUA NOTA FINAL É: {vtotal:.1f}")

if vtotal >= 7:
    print(' \n * VOCÊ FOI APROVADO, PARABÉNS!')

elif vtotal < 7 and (vtotal > 5):
    print(' \n * VOCÊ ESTÁ DE EXAME, ESTUDE!')

if vtotal < 5:
    print(' \n * VOCÊ FOI REPROVADO!')