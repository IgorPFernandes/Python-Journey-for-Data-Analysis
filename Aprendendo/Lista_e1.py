# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

#ou

for num in list1:
    print(num)


# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

list2 = ["Igor",2.0,5,False,None]
print(list2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

name = "Igor"
surname = "Pereira"
fullname = name + " " + surname
print(fullname)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tup = (1,2,2,3,4,4,4,5)
print(tup.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela

disc1 = {}
print(disc1)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

disc1 = {"Igor":25,"Jão":24,"Alê":28}
print(disc1)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

#disc1.update({"Roberto":23})
#print(disc1)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

disc2 = {1:[2,3],2:2,3:3}
print(disc2)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
#frase = 'Cientista de Dados é o profissional mais sexy do século XXI'