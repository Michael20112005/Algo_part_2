def plant_pumpkins(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                print(f"Посаджений гарбуз на рядку {i}, стовпці {j}")
        else:
            for j in range(n - 1, -1, -1):
                print(f"Посаджений гарбуз на рядку {i}, стовпці {j}")