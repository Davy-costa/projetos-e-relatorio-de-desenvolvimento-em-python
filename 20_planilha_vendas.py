"""
Miniprojeto: Planilha de Vendas
--------------------------------
Simula uma planilha de vendas usando uma matriz (lista de listas),
onde cada LINHA representa um vendedor e cada COLUNA representa um mês.
"""

vendedores = ["Ana", "Bruno", "Carla"]
meses = ["Janeiro", "Fevereiro", "Março"]

vendas = [
    [1000, 1200, 900],   # Ana
    [800, 950, 1100],    # Bruno
    [1500, 1400, 1600],  # Carla
]


# ---------------------------------------------------------
# Etapa 1: percorrer a matriz e exibir cada valor
# ---------------------------------------------------------
for i in range(len(vendas)):
    for j in range(len(vendas[0])):
        print(f"Vendedor: {vendedores[i]} | Mês: {meses[j]} | Venda: {vendas[i][j]}")


print("========================================================================")
print("========================================================================")


# ---------------------------------------------------------
# Etapa 2: total de vendas por vendedor (loop externo = linha)
# ---------------------------------------------------------
print("etapa 2")

totais_vendedores = []

for i in range(len(vendas)):
    total_linhas = 0
    for j in range(len(vendas[0])):
        total_linhas += vendas[i][j]
    totais_vendedores.append(total_linhas)
    print(f"{vendedores[i]}: R$:{total_linhas}")


print("===============================================================")
print("===============================================================")


# ---------------------------------------------------------
# Etapa 3: total de vendas por mês (loop externo = coluna)
# ---------------------------------------------------------
print("Etapa 3: total de vendas por mês")
for j in range(len(vendas[0])):
    total_coluna = 0
    for i in range(len(vendas)):
        total_coluna += vendas[i][j]
    print(f"{meses[j]}: R$:{total_coluna} ")


print("===============================================================")
print("===============================================================")


# ---------------------------------------------------------
# Etapa 4: total geral da empresa
# ---------------------------------------------------------
print("etapa 4 total geral da empresa")
total_geral = sum(totais_vendedores)
print(f"Total geral: R$:{total_geral}")


print("========================================================================")
print("========================================================================")


# ---------------------------------------------------------
# Etapa 5: vendedor com maior total de vendas
# ---------------------------------------------------------
print("etapa 5")

maior = totais_vendedores[0]
indice_maior = 0

for i in range(1, len(totais_vendedores)):
    if totais_vendedores[i] > maior:
        maior = totais_vendedores[i]
        indice_maior = i

print(f"vendedor do ano foi: {vendedores[indice_maior]}!! que com seu esforço vendeu: R$:{maior}!")
