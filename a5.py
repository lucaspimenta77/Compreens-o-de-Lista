numeros_divisiveis = [numero for numero in range(1, 31) if numero % 3 == 0 and numero % 5 == 0]
print(f"Esses sao os numeros que podem ser divididos por 3 e 5: {numeros_divisiveis}")

numeros_divisiveis2 = [numero for numero in range(1, 31) if numero % 3 == 0 or numero % 5 == 0]
print(f"Esses sao todos os numeros que são divididos por 3 ou 5: {numeros_divisiveis2}")