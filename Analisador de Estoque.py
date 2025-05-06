def lista_de_produtos(estoque):#função com parametro estoque
    
   quantidade = len(estoque)# parametro variavel definindo a quantidade de itens no estoque usando len 
   print("Total de itens é:", quantidade) #impriminando quantidade de itens no estoque
    
   if "Sabonete" in estoque: #condição para saber se tem ou não o item no estoque 
       print("Sabonete"" está presente no estoque. ")
   else: 
       print(estoque,"não está presente no estoque.")


   print("Lista em ordem alfabética:")
   ordem = sorted(estoque)#colocando a lista estoque em ordem alfabetica com sorted e dando a ele a variavel ordem
   for item in ordem:# percorrendo cada item da lista ordem, que já está ordenada.
     print(item)
     
estoque = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Farinha",
    "Açúcar",
    "Sal",
    "Óleo",
    "Café",
    "Leite",
    "Achocolatado",
    "Bolacha",
    "Refrigerante",
    "Água Mineral",
    "Sabonete",
    "Shampoo",
    "Condicionador",
    "Papel Higiênico",
    "Detergente",
    "Esponja",
    "Sabão em Pó",
    "Desinfetante",
    "Escova de Dente",
    "Creme Dental",
    "Fralda",
    "Absorvente"
    ]
 
lista_de_produtos(estoque)


