def calcular_media_lista(lista):
   soma = sum(lista) 
   quantidade = len(lista)
   media = soma / quantidade 
   return media 

numeros = [10, 30, 50, 40, 60, 20]

resultado = calcular_media_lista(numeros)

print("A média dos valores é: ", resultado) 