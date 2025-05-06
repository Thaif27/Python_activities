
estoque = [ "Arroz", "Cuscuz", "Carne", "Cebola"]

for estoques in estoque:
    print(estoques)

estoque.append("Frango")
print("--------NOVO ESTOQUE--------")
for estoques in estoque:
    print(estoques)

estoque.remove("Cebola")
print("--------NOVA LISTA REMOVENDO UM ITEM--------")
for estoques in estoque:
    print(estoques)

print("Itens no estoque após remoção:", len(estoque))    