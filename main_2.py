pergunta = int(input("Voce quer ver o seu IMC ou a altura do triangulo?\n1 - Área do triangulo\n2 - IMC\n"))

if pergunta == 1:
    print("================================")
    print("        Área do triangulo")
    print("================================\n")

    altura_triangulo = int(input("Qual a altura do seu triangulo? "))
    print("================================\n")
    base_triangulo = int(input("Qual a base do seu triangulo? "))
    print("================================\n")
    area= print(f"A área do seu triangulo é: {(base_triangulo * altura_triangulo)/2}\n")

if pergunta == 2:
    print("================================")
    print("              IMC")
    print("================================\n")
    peso = float(input("Qual é o seu peso? "))
    print("================================\n")
    altura = float(input("Qual a sua altura? "))
    print("================================\n")

    imc = peso/(altura*altura)

    area= print(f"Seu IMC é: {imc}\n\n")

    if imc < 18.5:
            print("================================\n")
            print("está a baixo do peso\n")

    elif imc == 18.5 and imc < 24.9:
            print("================================\n")
            print("está com o peso normal\n")
            
    elif imc == 25.0 and imc < 29.9:
            print("================================\n")
            print("está com o sobrepeso\n")

    elif imc == 30.0 and imc < 34.9:
            print("================================\n")
            print("está com obsidade tipo 1\n")

    elif imc == 35.0 and imc < 39.9:
            print("================================\n")
            print("está com obsidade tipo 2\n")
            
    if imc > 40.0:
            print("================================\n")
            print("está com obsidade tipo 3\n")
