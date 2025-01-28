lista = [4,6,2,32,74,2,6,5,3,123,52,67,43,24,15]
n = len(lista)

for i in range(n):
    for j in range(0,n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)

