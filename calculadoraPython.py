print('**********Python calculator - made by Gabrielle Gomes**********')

print('Selecione o número da operação desejada: \n '
      '1 - Soma \n '
      '2 - Subtração \n '
      '3 - Multiplicação \n '
      '4 - Divisão')

opcao = float(input('Digite sua opção (1, 2, 3 ou 4): '))

num1 = float(input('Digite o primeiro número: '))

num2 = float(input('Digite o segundo número: '))


def soma(a, b):
    return float(a + b)


def subtracao(a, b):
    return float(a - b)


def multiplicacao(a, b):
    return float(a * b)


def divisao(a, b):
    return float(a / b)


if opcao == 1:
    print(soma(num1, num2))
elif opcao == 2:
    print(subtracao(num1, num2))
elif opcao == 3:
    print(multiplicacao(num1, num2))
else:
    print(divisao(num1, num2))
