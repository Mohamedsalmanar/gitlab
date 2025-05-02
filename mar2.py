#1)
matrix = [[10,20,30],[40,50,60],[70,80,90]]

for row in zip(*matrix):
    print(list(row))

transposed_matrix = [list(row) for row in zip(*matrix)]
print(transposed_matrix)

#2)

matrix = [  [10,20,30],
            [40,50,60],
            [70,80,90]
         ]

#3)

