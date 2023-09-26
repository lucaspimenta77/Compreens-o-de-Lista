texto = "Esta é uma frase de exemplo com várias palavras aleatorias escolhidas por mim"
palavras_mais_de_3_letras = [palavra for palavra in texto.split() if len(palavra) > 3]
print(palavras_mais_de_3_letras)
