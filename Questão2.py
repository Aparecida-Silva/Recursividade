numero = int(input("Digite um número inteiro: "))

def soma(resultado, numero):
    if (numero == 0):
        return resultado
    return soma(resultado + numero, numero - 1)
    
print("")
print("A soma de todos os valores a partir do número", numero, "até zero é: ", soma(0, numero))
