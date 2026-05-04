
nomes = ["Ana" , "Maria" , "Enzo" , "Leo"] # Determina posição de cada nome (0,1,2,3)

for i in range(len(nomes)): # 1°LOOP // len(nomes) - retorna os nomes // range(4) - gera 0,1,2,3 // i=0,i=1,i=2,i=3

    for j in range (i + 1, len(nomes)): # 2°LOOP // j sempre começa em i+1 - pegas os nomes depois do atual

        print(nomes[i], "e" , nomes[j]) # imprime nome atual do [i] "e" imprime nome atual do [j]
