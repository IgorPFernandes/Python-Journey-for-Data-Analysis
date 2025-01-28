#--- Inicialização ---
print("Bem-Vindo à Calculadora")

# Lista para validar a operação selecionada pelo usuario
operacoes_validas = ["+","-","/","*","^"]
while True:
    operacao = input("Escolha a operação ( + , - , / , * , ^ )")
    if operacao in operacoes_validas:
        break
    else:
        print("Operação inválida! Tente novamente.")

num1 = float(input("Informe o primeiro número da operação"))
num2 = float(input("Informe o segundo número da operação"))

# Casos de cada operação
if operacao == "+":
    resultado = num1+num2
    print("O resultado é:",resultado)
elif operacao == "-":
    resultado = num1-num2
    print("O resultado é:",resultado)
elif operacao == "/":
    resultado = num1/num2
    print("O resultado é:",resultado)
elif operacao == "*":
    resultado = num1*num2
    print("O resultado é:",resultado)
elif operacao == "^":
    resultado = num1**num2
    print("O resultado é:",resultado)

