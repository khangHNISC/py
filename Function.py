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


# default argument
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# with keyword argument
# ask_ok('y', retries=5)
# 1. position or keyword args
# 2. keyword only
# 3. positional only

# Arbitrary arguments list
def concat(*args, sep="/"):
    return sep.join(args)
