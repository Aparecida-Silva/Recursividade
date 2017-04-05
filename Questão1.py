Num1 = int(input("Digite o primeiro número inteiro para ser exibido: "))
Num2 = int(input("Digite o segundo número inteiro para ser exibido: "))

def Imprima(Num1, Num2):
   print(Num1)
   if (Num1 == Num2):
       return Num2
   return Imprima(Num1 + 1, Num2)
   
Imprima(Num1, Num2)
