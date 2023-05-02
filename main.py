def adicao(numeros: list) -> float:
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


def subtracao(numeros: list) -> float:
    if len(numeros) > 2:
        return 'Passe apenas 2 numeros para essa operação, Ex: "[num1, num2]" retorna "num1 - num2"'
    return numeros[0] - numeros[1]


def multiplicacao(numeros: list) -> float:
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado


def calculadora_vc(numeros: list, operacao: str) -> float:
    if operacao == 'adicao':
        return adicao(numeros)
    if operacao == 'subtracao':
        return subtracao(numeros)
    if operacao == 'multiplicacao':
        return multiplicacao(numeros)
    # divisao
    # exponenciacao
    # fatoracao
    return 'Essa operação não existe (ainda)'


print(calculadora_vc([4, 212983.782398, -2.567], 'adicao'))
