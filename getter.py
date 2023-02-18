from input_validator import validate_choice, validate_file_name, validate_matrix_row


def get_choice(subject):
    print("Необходимо ввести {}: 1 - с клавиатуры, 2 - из файла".format(subject))
    choice = input().strip()
    while not validate_choice(choice):
        choice = get_choice(subject)
    return choice


def get_value(text):
    print(text)
    value = input().strip()
    return value


def get_filename():
    filename = get_value("Введите название файла:")
    while not validate_file_name(filename):
        filename = get_value("Введите название файла:")
    return filename


def get_matrix(size):
    matrix = []
    print("Введите коэффициенты матрицы по рядам в количестве {}:".format(str(size + 1)))
    for i in range(size):
        try:
            row = [i for i in input().split()]
            while not validate_matrix_row(row, size):
                row = [i for i in input().split()]
            row = [float(i) for i in row]
            matrix.append(row)
        except ValueError:
            print("Матрица должна содержать только числа")
    return matrix


def get_matrix_from_file(filename, size):
    matrix = []
    with open(filename, "r") as file:
        lines = file.readlines()
        if len(lines) <= 1:
            print("Файл пустой!")
        for i in range(1, len(lines)):
            try:
                row = [float(i) for i in lines[i].split()]
                if validate_matrix_row(row, size):
                    matrix.append(row)
                else:
                    matrix = []
                    break
            except ValueError:
                print("Матрица должна содержать только числа")
    return matrix


def read_one_string_from_file(filename):
    with open(filename, "r") as file:
        a = file.readline()
        return a
