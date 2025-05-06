
my_list = [10,20,30,40,50] #lista com números inteiros

for numero in my_list: #loop para percorrer os números na minha lista e imprimir
    print(numero)

my_list.append(60) #adicionando o numero 60 ao final da lista
print("Adicionando o número 60: ", my_list)

for numero in my_list: # loop para percorrer a lista depois da adição 
    print(numero)

my_list.remove(10) #remover o numero 10 
print("Removendo o número 10: ", my_list)

for numero in my_list:# loop para percorrer a lista depois da remoção 
    print(numero)