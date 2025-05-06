senha = "python123"

while True:
    digitar_senha = input("digite sua Senha: ")

    if digitar_senha == senha: #comparando a senha colocada pelo usuario e senha já existente.
       print("Acesso Liberado")
       break
    else:
      print("Senha incorreta. Tente novamente.") 




