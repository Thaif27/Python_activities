
numero = int(input("Digite um número: "))
def verificar_numero(numero):
    if numero > 0: 
         print("O número é Positivo.")
    elif numero < 0:
         print("O número é Negativo.")
    else:
         print("O número é Zero.")
verificar_numero(numero)