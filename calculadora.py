Valor1 = input("Digite um numero: ")
Valor2 = input("Digite um numero: ")
convert1 = int(Valor1)
convert2 = int(Valor2)
soma = convert1 + convert2
multi = convert1 * convert2
divisao = convert1/convert2
subtraçao = convert1 - convert2
resultado = input("Escolha uma operação matematica: multiplicação,subtração,divisão ou soma: ")
if resultado=="soma":
  print(soma)
elif resultado=="multiplicação":
  print(multi)
elif resultado=="divisão":
  print(divisao)
elif resultado=="subtração":
  print("Resultado:",subtraçao)
else:
  print("escreva novamente a operação")
