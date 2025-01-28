#Lista abre e fecha colchetes []
#Lista inteiros
list1 = [1,2,6,12,62,86,123,63,12]
#Lista Strings
list2 = ["arroz","feijão","frango"]
#Lista mista
list3 = [3,"arroz",5,"feijão",1,"frango"]
#deletar
#del list1[9]
#deletar sempre o último
#del list2[len(list2)-1]

#print(len(list1))

#Lista aninhada

listn = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(listn)):
    for j in range(len(listn[i])):
        print(listn[i][j])


print(63 in list1)
print(max(list1))
print(min(list1))

#Adiciona
#list2.append("frango")
print(list2)
list4 = []
for item in list1:
    list4.append(item)

print(list4)
# Encontra o índice do valor
print(list4.index(123))

# Inserir por índice
#list4.insert(3,4)
#print(list4)

# Inserir no final
#list4.extend([124])
#print(list4)

# Remover valor especifico
#list4.remove(124)

disc1 = {"Igor":25, "Alê":28, "Roberto":23, "Jão":24}
print(disc1)
# Resulta no que está agregado a 'Igor'
print(disc1['Igor'])

#Os discionários também podem ser aninhados assim como listas
#Vale lembrar que arquivos como JSON(Java Script Object Notation) é um tipo de discionário

#Uma tupla é uma lsita que não pode ser modificada, resumidamente, 