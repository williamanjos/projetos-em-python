def calculadora ()
    print("selecione a operação ")
    print ("1 - soma")
    print ("2 - subtração")
    print ("3 - multiplicação")
    print ("4 - divisão")

escolha = input("digite o número da operação: ")
if escolha in ["1", "2", "3", "4"]:
    num1= float(input("digite o primeiro número: "))
    num2= float(input("digite o segundo número: "))

    if escolha =="1":
        resultado = num1+num2
    elif escolha =="2":
        resultado = num1-num2
    elif escolha =="3":
        resultado = num1*num2   
    elif escolha =="4":
        if num2 != 0:
            resultado = num1/num2
        else:
            return "Erro: Divisão por zero não é permitida."
        
    print(f"O resultado é: {resultado}")

else:
    print("Opção inválida. Por favor, escolha uma operação válida.")

    calculadora()
            
