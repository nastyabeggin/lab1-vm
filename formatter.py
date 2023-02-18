import numpy as np
from tabulate import tabulate


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_matrix(matrix):
    print(f"{Colors.HEADER}Матрица:{Colors.END}")
    print(tabulate(matrix))


def print_results(matrix, a, x_current, max_dif, k):
    print("----------------------")
    print(f"{Colors.GREEN}Результаты вычислений:{Colors.END}")

    print(f"{Colors.BOLD}Заданная точность:{Colors.END} %.10f" % a)

    base_print(matrix, x_current, max_dif, k)


def print_intermediate_results(matrix, x_current, max_dif, k):
    print("----------------------")
    print(f"{Colors.CYAN}Промежуточные результаты вычислений:{Colors.END}")

    base_print(matrix, x_current, max_dif, k)


def base_print(matrix, x_current, max_dif, k):
    print(f"{Colors.BOLD}Полученные векторы неизвестных:{Colors.END}")
    for number in x_current:
        print(np.around(number, 6), end="\t")
    print()

    print(f"{Colors.BOLD}Количество итераций:{Colors.END} %d" % k)
    print(f"{Colors.BOLD}Максимальная разница между итерациями:{Colors.END} %.10f" % np.around(max_dif, 10))
    print_discrepancy(matrix, x_current)


def print_discrepancy(matrix, x_current):
    print(f"{Colors.BOLD}Невязки:{Colors.END}", end=' ')
    for row in matrix:
        print(np.around(row[-1] - np.sum(np.multiply(np.array(row[: len(row) - 1]), np.array(x_current))), 6), end=" ")
    print()
