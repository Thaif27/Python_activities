numeros = [1, 4, 7, 10, 12, 16]

pares = []
impares = [] 

i = 0

while i <len(numeros):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
        print("número ", numeros[i], "é Par")
    
    elif numeros[i] % 2 != 0: #poderia ser else mas preferi usar elif porque sim. 
        impares.append(numeros[i])
        print("números ", numeros[i],"é Impar" )
    i += 1     
   
print("\nNúmeros pares:")
for p in pares:
    print(p)

# Imprimindo todos os ímpares
print("Números ímpares:")
for i in impares:
    print(i)

print("Quantidade de Pares: ", len(pares))
print("Quantidade de Ímpares: ", len(impares))

    

