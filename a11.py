nomes = ["Ana", "Bruna", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Hélio", "Isabela", "João Antonio", "Lucas", "Marcia", "Jailson", "Vladmir", "Levi", "Gabigol", "Cristiano Ronaldo"]
vogais = "AEIOUaeiou"
nomes_sem_vogais = []

for nome in nomes[:10]:
    nome_sem_vogais = ''.join([letra for letra in nome if letra not in vogais])
    nomes_sem_vogais.append(nome_sem_vogais)

print(nomes_sem_vogais)
