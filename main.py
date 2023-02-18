from input_validator import *
from getter import *
from solver import *

choice = get_choice("точность").strip()

accuracy = 1
if choice == "1":
    accuracy = get_value("Введите точность:")

    while not validate_accuracy(accuracy):
        print("Точность не валидна")
        accuracy = get_value("Введите точность:")

elif choice == "2":
    while True:
        filename = get_filename()

        accuracy = read_one_string_from_file(filename)
        if not validate_accuracy(accuracy):
            print("Точность из файла не валидна")
            continue
        break

choice = get_choice("размерность матрицы")

dimension = 1
if choice == "1":
    dimension = get_value("Введите размерность матрицы:")

    while not validate_dimension(dimension):
        print("Размерность матрицы не валидна")
        dimension = get_value("Введите размерность матрицы:")

elif choice == "2":
    while True:
        filename = get_filename()

        dimension = read_one_string_from_file(filename)
        if not validate_dimension(dimension):
            print("Размерность матрицы из файла не валидна")
            continue
        break

accuracy = float(accuracy)
dimension = int(dimension)
matrix = []

choice = get_choice("коэффициенты матрицы")
if choice == "1":
    matrix = get_matrix(dimension)
elif choice == "2":
    while not matrix:
        filename = get_filename()
        matrix = get_matrix_from_file(filename, dimension)

print_matrix(matrix)
iterate_matrix(matrix, accuracy, dimension)
