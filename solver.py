from formatter import *


def check_diagonal(matrix, size):  # проверка диагонального преобладания
    for i in range(size):
        sumo = 0
        for j in range(size):
            sumo += abs(matrix[i][j])
        if abs(matrix[i][i]) < (sumo - abs(matrix[i][i])):
            return False
    return True


def is_it_possible_to_get_diagonal(matrix, size):
    for i in range(size):
        flag = False
        sumo = sum(abs(i) for i in matrix[i][: size - 1])
        for j in range(size - 1):
            if abs(matrix[i][j]) >= sumo - (abs(matrix[i][j])):
                flag = True
        if not flag:
            return False
    return True


def check_zero_rows(matrix, size):
    if [0] * (size + 1) in matrix:
        return True
    else:
        return False


def get_diag_matrix(matrix, size):  # вычисление матрицы с диагональным преобладанием
    for i in range(len(matrix) - 1):
        maxi = -1
        minn = 10 ** 20
        k = -1
        for j in range(i + 1, len(matrix)):
            sum_of_row = sum(map(abs, matrix[j][: size]))
            sum_after_element = sum(map(abs, matrix[j][j:]))
            if abs(matrix[j][i]) >= sum_of_row - abs(matrix[j][i]) \
                    and abs(matrix[j][i]) >= maxi \
                    and sum_after_element <= minn:
                maxi = matrix[j][i]
                minn = sum_after_element
                k = j
        if k != -1:
            matrix[i], matrix[k] = matrix[k], matrix[i]

    return matrix


def iterate_matrix(matrix, accuracy, size):
    if is_it_possible_to_get_diagonal(matrix, size):
        if not check_diagonal(matrix, size):
            matrix = get_diag_matrix(matrix, size)
        if not check_diagonal(matrix, size):
            print(f"{Colors.FAIL}Невозможно привести матрицу к диагональному виду{Colors.END}")
        else:
            print(f"{Colors.CYAN}\nПосле перестановки строк\n{Colors.END}")
            print_matrix(matrix)
            c = [[0] * size for _ in range(size)]  # матрица с коэффициентами подсчитанными по спец. формуле
            vector = [0] * size  # начальное приближение x^0, используется в формуле для нахождения векторов неизвестных

            for i in range(size):
                vector[i] = matrix[i][size] / matrix[i][i]  # vector[i] = d[i] в формуле d = b / a
                for j in range(size):  # заполняем матрицу C
                    if i != j:
                        c[i][j] = (-1) * matrix[i][j] / matrix[i][i]
                    else:
                        c[i][j] = 0

            x_current = [0] * size  # настоящая итерация x
            x_previous = vector  # предыдущая итерация x, нулевое приближение для 1й итерации
            x_max = [0] * size  # хранение разниц между последней и предпоследней итерациями
            k = -1  # номер итерации

            while True:  # пока максимальная разница между элементами не станет меньше или равна точности
                k += 1
                x_previous = x_current
                x_current = [0] * size

                for i in range(size):  # заполняем настоящую итерацию
                    for j in range(size):
                        x_current[i] += c[i][j] * x_previous[j]  # проходим по x внутри формулы
                    x_current[i] += vector[i]

                for i in range(size):  # критерий по абсолютному отклонению
                    x_max[i] = abs(x_current[i] - x_previous[i])

                if max(x_max) <= accuracy:
                    break
                else:
                    print_intermediate_results(matrix, x_current, max(x_max), k)

            print_results(matrix, accuracy, x_current, max(x_max), k)
    else:
        print(f"{Colors.FAIL}Невозможно привести матрицу к диагональному виду{Colors.END}")
