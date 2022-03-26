# Ловим ошибку
x = "lion"


def fun1(obj, index):
    return obj[index]


def catcher():
    try:
        fun1(x, 4)
    except IndexError:
        print("Catched!")


print(catcher())

# Вызываем ошибку
try:
    raise ValueError
except ValueError:
    print('Catched!')

# Конструкция try/finally
try:
    fun1(x, 3)
finally:
    print("All ok, try more!")

# Проверяем на True/False
assert fun1(x1, 3), "Haha, catched!"
