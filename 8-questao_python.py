8.def calcular_imc(peso, altura):
    altura_em_metros = altura / 100  
    imc = peso / (altura_em_metros ** 2)
    return imc


def avaliar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"


print("Bem-vindo à Calculadora de IMC!")
peso = float(input("Por favor, digite seu peso (em quilogramas): "))
altura = float(input("Agora, digite sua altura (em centímetros): "))


imc = calcular_imc(peso, altura)


classificacao = avaliar_imc(imc)


print(f"Seu IMC é {imc:.2f} e sua classificação é: {classificacao}")


