import numpy as np
from itertools import permutations
import time

best_path=''
now_path=''
num_best = 999999



# Функция для вычисления длины пути коммивояжера
def calculate_path_length(matrix, path):
    length = 0
    for i in range(len(path) - 1):
        length += matrix[path[i], path[i+1]]
    # Возвращение к начальной точке
    length += matrix[path[-1], path[0]]
    return length

def min_in_row(matrix,i):
    res=min(matrix[i,:])
    return res

def min_in_column(matrix,i):
    res=min(matrix[:,i])
    return res

def reduce(matrix,size):
    for i in range(size):
        k=min_in_row(matrix,i)
        if k > 110:
            continue
        for j in range(size):
            matrix[i,j]-=k
    for i in range(size):
        k=min_in_column(matrix,i)
        for j in range(size):
            matrix[j,i]-=k
    return matrix

def reduce_count(matrix,size):
    count = 0
    for i in range(size):
        k=min_in_row(matrix,i)
        if k > 110:
            continue
        count += int(k)
        for j in range(size):
            matrix[i,j] -= int(k)
    for i in range(size):
        k=min_in_column(matrix,i)
        count += int(k)
        for j in range(size):
            matrix[j,i] -= int(k)
    return int(count)

def nearest_neighbor(matrix, start_column_index, size):
    path=''
    visited = [False] * size
    visited[start_column_index] = True
    current_city = start_column_index
    length = 0

    for _ in range(size - 1):
        next_city = np.argmin([matrix[current_city][i] if not visited[i] else np.inf for i in range(size)])
        length += matrix[current_city][next_city]
        visited[next_city] = True
        current_city = next_city
        path+=str(next_city)

    # Вернуться к начальному городу
    length += int(matrix[current_city][start_column_index])

    return path, length

def min_appr(matrix,size):
    length=9999999
    path=''
    for i in range(size):
        temp_path, temp_length = nearest_neighbor(matrix, i, size)
        length=min(length,temp_length)
        if temp_length == length:
            path = temp_path
    print(length,path)
    return length, path

def deletion(matrix,size,index1,index2):
    for i in range(size):
        matrix[index1,i] = 9999
        matrix[i,index2] = 9999
    return matrix

def grade(matrix,size):
    index1, index2 = 0, 0
    best_num = 999999
    for i in range (size):
        for j in range (size):
            if matrix[i, j] == 0:
                temp_matrix = deletion(matrix,size,i,j)
                temp = reduce_count(temp_matrix,size)
                if temp < best_num:
                    temp = best_num
                    index1 = i
                    index2 = j
                else:
                    continue
            else:
                continue
    return index1, index2

def optimizer(matrix, size, now, temp_path, num_best):
    lower = reduce_count(matrix, size)
    temp_matrix = reduce(matrix, size)
    num_best = int(num_best)

    if lower + now > num_best:
        return None, None
    else:
        if np.array_equal(temp_matrix, matrix):
            return now, temp_path
        else:
            index1, index2 = grade(temp_matrix, size)
            temp_matrix1 = deletion(temp_matrix, size, index1, index2)
            i, j = optimizer(temp_matrix1, size, now + lower, temp_path + str(index2), num_best)
            if i is not None and j is not None:
                num_best = i
                best_path = j
            temp_matrix2 = temp_matrix.copy()
            temp_matrix2[index1, index2] = 99999
            h, k = optimizer(temp_matrix2, size, now, temp_path, num_best)
            if h is not None and k is not None:
                num_best = h
                best_path = k
    return num_best, best_path
def main():
    total_solved = 0
    start_time = time.time()
    n=int(input('n'))
    
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
        print(f"Matrix size: {n}x{n}")
        best_path, num_best = min_appr(matrix,n)
        num_best, best_path = optimizer(matrix, n,0, '',num_best)
        print(best_path, num_best)
        
        total_solved += 1

    print(f"Total matrices solved: {total_solved}")


if __name__ == "__main__":
    main()
