soma = 0
quantidade = 0

while True: 
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break 

    soma += numero 
    quantidade += 1

print("Você digitou", quantidade, "números.") 
print("A soma total é", soma)



