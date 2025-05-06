

gastos = [] #Armazenar lista de gastos

categorias = [] #Armazenar lista de categorias

quantidade = int(input("Quantos gastos você teve hoje? ")) #pede a quantidade de gastos para rodar no laço

for i in range(quantidade): #laço for de acordo com a quantidade de gastos ele vai rodar uma nova entrada 
    valor = float(input(f"Gasto {i+1}: Qual o valor? ")) #valores dos gastos
    categoria = input("Categoria: " )#categoria dos gastos
    gastos.append(valor)# lembrar append adciona a variavel lista cada valor que for inserido e rodado
    categorias.append(categoria)# aqui append faz o mesmo mas com categorias inseridas 



total = sum(gastos)#sum calcula todos os gastos, lembre
#sempre que ele deve estar no canto da tela fora do laço 
#for para não dar erro e imprimir o valor a cada recebimento

print(f"\n Total gasto hoje: R$ {total:.2f}") # imprimi o gasto total já calculado lembrando que
# .2f faz imprimir o total com duas casas decimais no formato padrão com ponto