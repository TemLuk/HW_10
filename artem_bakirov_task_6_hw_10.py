def example1():
    print("\nExample 1")
    try:
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', round(x / y, 2))
    except ZeroDivisionError:
        print("ZeroDivisionError, не дели на ноль")
    except ValueError:
        print("ValueError, я такого не знаю, используй инт)")


def example2(L):
    print("\nExample 2")
    sum_of_pairs = []
    try:
        sum_of_pairs.append(L[0] + L[1])
        sum_of_pairs.append(L[2] + L[3])
        sum_of_pairs.append(L[4] + L[5])
        sum_of_pairs.append(l[4] + L[5])
    except TypeError:
        print("TypeError, если складываешь разные типа данных - используй конкатенацию")
    except NameError:
        print("NameError, правильно называй название")
    else:
        print("sumOfPairs = ", sum_of_pairs)


def example3(file_name):
    print("\nExample 3")
    try:
        with open(file_name, "w+") as f:
            f.write(file_name.upper())
    except FileNotFoundError:
        print("Ваш файл ненайден")
    except FileExistsError:
        print("Этот файл уже существует")
    else:
        print("Файл создан")


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example3("doesNotExistYest.txt")
    example3("./Dessssktop/misspelled.txt")


main()