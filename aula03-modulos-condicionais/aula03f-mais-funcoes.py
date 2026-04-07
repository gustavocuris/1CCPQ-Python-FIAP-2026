def boas_vindas (nome):
    print(f"Olá, {nome}!! Seja bem-vindo!")

nome_digitdo = input("Digite seu nome: ")
boas_vindas (nome_digitdo)

# FUNÇÃO COM PARAM. COM RETORNO

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma (1, 2)
print(resultado_soma)

