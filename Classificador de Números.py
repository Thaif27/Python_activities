def classificar_numeros(numeros): 
   pares = []
   impares = []

   for numero in numeros:
       if numero % 2 == 0:
           pares.append(numero)
       else:
           impares.append(numero)
     

   media1 = sum(pares) / len(pares) if len(pares) > 0 else 0 
   media2 = sum(impares) / len(impares) if len(impares) > 0 else 0



   print("Números pares:", pares)
   print("Quantidade de pares:", len(pares))
   print("Média dos pares:", media1 )
   print("Números Ímpares:", impares)
   print("Quantidade de Ímpares:", len(impares))
   print("Média dos Impares: ", media2)


numeros = [17, 4, 23, 8, 15, 2, 31, 6, 9, 12, 19, 10]

classificar_numeros(numeros)
