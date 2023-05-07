import os

def clear():{
    os.system('cls||clear')
}
clear()
pergunta = int(input("Voce quer ver o seu IMC ou a altura do triangulo?\n1 - Área do triangulo\n2 - IMC\n>>>"))

# Triangle/ Triângulo

if pergunta == 1:
    clear()
    altura_triangulo = int(input("Qual a altura do seu triangulo?\n>>>"))
    clear()
    base_triangulo = int(input("Qual a base do seu triangulo?\n>>>"))
    print("================================\n")
    area= print(f"A área do seu triangulo é: {(base_triangulo * altura_triangulo)/2}\n")

#IMC

if pergunta == 2:
    clear()
    peso = float(input("Qual é o seu peso?\n>>>"))
    clear()
    altura = float(input("Qual a sua altura?\n>>>"))
    imc = peso/(altura*altura)
    clear()
    area= print(f"Seu IMC é: {imc:.2f}\n\n")

    if imc < 18.5:
        print("================================\n")
        print("está abaixo do peso\n")
    elif imc < 24.9:
        print("================================\n")
        print("está com o peso normal\n")
    elif imc < 29.9:
        print("================================\n")
        print("está com o sobrepeso\n")
    elif imc < 34.9:
        print("================================\n")
        print("está com obsidade tipo 1\n")
    elif imc < 39.9:
        print("================================\n")
        print("está com obsidade tipo 2\n")
    else:
        print("================================\n")
        print("está com obsidade tipo 3\n")
