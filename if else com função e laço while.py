
numero = int(input("Digite um número: "))
def verificar_numero(numero):
    if numero > 0: 
         print("O número é Positivo.")
    elif numero < 0:
         print("O número é Negativo.")
    else:
         print("O número é Zero.")

while True: #inicia um laço infinito, ele vai se repetir até o break. 
            #É usado aqui para manter o programa rodando até o usuário digitar "sair".
         entrada = input("Digite um numero ou 'sair' para encerrar: ")
         

         if entrada.lower() == "sair" : #converte a entrada letras minúsculas com .lower() para aceitar "Sair" "SAIR" e assim por diante.
              print("Programa foi encerrado.") 
              break #sai imediatamente do laço while, sem ele o programa continuaria rodando. 

         if entrada.lstrip('-').isdigit(): #Aqui ele verifica se a entrada é um número inteiro válido remove um possível 
                                           #sinal de menos no início, como em -5, verifica se o que sobrou são só dígitos (números).
              numero = int(entrada)
              verificar_numero(numero)
         else:
              print("Entrada inválida digite um número inteiro ou 'sair." )