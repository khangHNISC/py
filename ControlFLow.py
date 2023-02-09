def what_if_x_greater_than_0(v):
    if v < 0:
        print('Negative changed to zero')
    elif v == 0:
        print('Zero')
    elif v == 1:
        print('Single')
    else:
        print('More')


if __name__ == '__main__':
    # x = int(input("Please enter an integer: "))
    # what_if_x_greater_than_0(x)

    # for using iter
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

    # range
    for i in range(5):
        print(i)

    for i in range(len(words)):
        print(i, words[i])

    # break and continue
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
        else:  # when no break occurs
            print(n, 'is prime')

    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)
