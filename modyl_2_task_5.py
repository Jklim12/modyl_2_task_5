def get_matrix (n,m,value):
    matrix = []
    for i in range(n):
        sub_matrix = []
        for j in range(m):
            sub_matrix.append(value)
        matrix.append(sub_matrix)
    return matrix

result_matrix = get_matrix(2, 2, 10)

  # Создаем матрицу
print(result_matrix)  # Выводим результат
