# SISTEMA DE NOTA PONDERADA FIAP
n1 = float(input("Digite NOTA, primeiro trimestre: ").replace(',', '.'))
n2 = float(input("Digite NOTA, segundo trimestre: ").replace(',', '.'))
n3 = float(input("Digite NOTA, terceiro trimestre: ").replace(',', '.'))

# ARREDONDAMENTO DE NOTAS
# n1
if (n1 - int(n1)) >= 0.7:  # PEGA APENAS A PARTE DECIMAL DO NÚMERO
    n1 = int(n1) + 1  # PEGA APENAS A PARTE INTEIRA DO NÚMERO

# n2
if (n2 - int(n2)) >= 0.7:  # PEGA APENAS A PARTE DECIMAL DO NÚMERO
    n2 = int(n2) + 1  # PEGA APENAS A PARTE INTEIRA DO NÚMERO

# n3
if (n3 - int(n3)) >= 0.7:  # PEGA APENAS A PARTE DECIMAL DO NÚMERO
    n3 = int(n3) + 1  # PEGA APENAS A PARTE INTEIRA DO NÚMERO

# CALCULO DAS MÉDIAS
vnotas = n1 * 3 + n2 * 2 + n3 * 5

vtotal = vnotas / 10

# PRINTS
print(f"SUA NOTA FINAL É: {vtotal:.2}")

if vtotal >= 6:
    print('VOCÊ FOI APROVADO, PARABÉNS!')

elif vtotal < 6 and (vtotal > 3):
    print('VOCÊ ESTÁ DE EXAME, ESTUDE!')

if vtotal < 3:
    print('VOCÊ FOI REPROVADO!')