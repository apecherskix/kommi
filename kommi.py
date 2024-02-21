import time
import numpy as np
from itertools import permutations
n = int(input('n'))



# Функция для вычисления длины пути коммивояжера
def calculate_path_length(matrix, path):
    length = 0
    for i in range(len(path) - 1):
        length += matrix[path[i], path[i+1]]
    # Возвращение к начальной точке
    length += matrix[path[-1], path[0]]
    return length

# Генерация всех возможных маршрутов


# Поиск маршрута с минимальной длиной
def solve(matrix):
    paths = permutations(range(n))
    min_length = float('inf')
    min_path = None
    for path in paths:
        current_length = calculate_path_length(matrix, path)
        if current_length < min_length:
            min_length = current_length
            min_path = path
    return min_path, min_length

def main():
    total_solved = 0
    start_time = time.time()
    
    while time.time() - start_time < 10:  # 5 minutes
        #matrix = np.random.randint(0, 101, size=(n, n))
        matrix = np.array([
        [37, 45, 82, 14, 23, 68, 91, 59, 3, 77],
        [12, 84, 51, 30, 9, 67, 42, 56, 20, 95],
        [72, 63, 38, 80, 26, 18, 50, 98, 33, 1],
        [22, 96, 7, 70, 65, 87, 49, 10, 27, 94],
        [47, 5, 75, 29, 43, 6, 79, 61, 32, 57],
        [69, 88, 36, 85, 2, 44, 13, 16, 81, 71],
        [99, 40, 19, 28, 64, 76, 54, 83, 46, 17],
        [11, 93, 34, 62, 53, 86, 24, 90, 15, 41],
        [4, 78, 21, 92, 66, 8, 25, 35, 55, 58],
        [48, 60, 74, 52, 89, 97, 39, 73, 31, 100]
    ])
        for k in range(n):
            matrix[k, k] = 9999
        best_path,num_best = solve(matrix)
        print(best_path, num_best)
        
        total_solved += 1

    print(f"Total matrices solved: {total_solved}")


if __name__ == "__main__":
    main()
