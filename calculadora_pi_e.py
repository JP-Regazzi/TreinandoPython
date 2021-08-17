def calculadora_algarismos_pi(n):
    soma = 0
    for x in range(1, 1 + n):
        soma += 1/x**2
    return (6 * soma)**0.5


def calculadora_de_e(n):
    soma = 0
    fatorial = 1
    for x in range(1, n + 1):
        fatorial *= x
        soma += 1/fatorial
    return soma


print(calculadora_algarismos_pi(int(input('Digite qual valor de k, para calcular pi '))))
print(calculadora_de_e(int(input('Digite qual valor de k, para calcular e '))))
