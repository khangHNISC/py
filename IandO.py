import math

if __name__ == '__main__':
    a = 2016
    b = 'Referendum'
    c = f'Results of the {a} {b}'
    print(c)

    # : minimum number of character wide
    print(f'The value of pi is approximately {math.pi:.3f}.')
    print('We are the {} who say "{}!"'.format('knights', 'Ni'))
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
    print('This {number:d} is {adjective}.'.format(number=16, adjective='absolutely horrible'))


