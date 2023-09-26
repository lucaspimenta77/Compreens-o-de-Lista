def is_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for divisor in range(3, int(numero ** 0.5) + 1, 2):
            if numero % divisor == 0:
                return False
        return True

numeros_primos = [numero for numero in range(1, 21) if is_primo(numero)]
print(numeros_primos)
