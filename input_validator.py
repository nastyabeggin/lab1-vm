import os


def validate_choice(choice):
    if choice in ["1", "2"]:
        return True
    else:
        return False


def validate_file_name(name):
    if os.path.isfile(name):
        return True
    print("Такого файла не существует")
    return False


def validate_accuracy(accuracy):
    try:
        if float(accuracy) > 0:
            return True
        return False
    except ValueError:
        return False


def validate_dimension(dimension):
    try:
        if 2 <= int(dimension) <= 20:
            return True
        return False
    except ValueError:
        return False


def validate_matrix_row(row, size):

    if len(row) != size + 1:
        print("Вы ввели неверное количество коэффициентов")
        return False
    for i in row:
        try:
            float(i)
        except ValueError:
            print("Матрица должна содержать только числа")
            return False
    return True
