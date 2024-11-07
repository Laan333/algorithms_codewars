def fibonacci(n: int) -> int:
    if n == 0:
        return 0  # первое число Фибоначчи (fibonacci(0)) - это 0
    elif n == 1:
        return 1  # второе число Фибоначчи (fibonacci(1)) - это 1
    a = 0  # первое число (fibonacci(0)) = 0
    b = 1  # второе число (fibonacci(1)) = 1
    for i in range(2, n + 1):  # начинаем с 2, так как 0 и 1 уже заданы
        c = a + b
        a = b
        b = c
    return b


d = fibonacci(2)
print(d)