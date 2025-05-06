
idade = int(input("Digite a sua Idade:"))

if idade >= 0 and idade <=12: 
   print("Você é Criança.")

elif idade >= 13 and idade <= 17:
   print("Você é Adolescente") 

elif idade >= 18 and idade <= 59:
   print("Você é Adulto")

elif idade >= 60:
 print("Você é Idoso")

else:
 print("Idade inválida")