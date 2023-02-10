def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        x = a + b
        for i in range(3, n):
            x = a + b
            a, b = b, x
        else:
            return x
