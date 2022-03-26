def divide():
    try:
        x = int(input('Введите первый аргумент:'))
        y = int(input('Введите второй аргумент:'))
        return x/y
    except ValueError:
        print('Catched')
    except ZeroDivisionError:
        print("ай яй яй делить на ноль можно не многим")
    finally:
        print(" I 'am happy that you learn python")



print(divide())
