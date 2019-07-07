from termcolor import cprint, colored
from random import randint

INDENT = ' ' * 2


def pad(str, length, padder=' '):
    while len(str) < length:
        str = padder + str
    return str


def print_rank(list, color, head=''):
    if head != '':
        cprint(head, color, attrs=['bold'])
    for i, item in enumerate(list):
        cprint(f'{INDENT}{pad(str(i + 1), len(str(len(list))))}:{INDENT}{item}', color)


def insert_elems(start, list, index):
    list = list[::-1]
    for item in list:
        start.insert(index, item)
    return start


def is_better(a, b):
    reversed = True if randint(0, 1) == 1 else False
    while True:
        cprint('Which is better? ', 'cyan', end='')
        if not reversed:
            cprint(str(a), 'yellow', end='')
            cprint(' or ', 'cyan', end='')
            cprint(str(b), 'yellow', end='')
        else:
            cprint(str(b), 'yellow', end='')
            cprint(' or ', 'cyan', end='')
            cprint(str(a), 'yellow', end='')
        cprint(': ', 'cyan', end='')

        user_input = input()

        if user_input == str(a):
            return True
        elif user_input == str(b):
            return False
        else:
            cprint('Invalid choice. Choose again.', 'red')


def rank(elems):
    if len(elems) <= 1:
        return elems
    elif len(elems) == 2:
        if is_better(elems[0], elems[1]):
            return elems
        else:
            return elems[::-1]

    middle = elems[0]
    less = []
    more = []
    for item in elems[1:]:
        if is_better(middle, item):
            less.append(item)
        else:
            more.append(item)

    less = rank(less)
    more = rank(more)

    return more + [middle] + less


cprint('Item ranker by comparison\n', 'yellow', attrs=['bold'])

start = int(input(colored('Enter the first integer of the list: ', 'yellow')))
end = int(input(colored('Enter the last integer of the list: ', 'yellow')))
print()

list = [n for n in range(start, end + 1)]

print_rank(rank(list), 'green', head='\nRanking Results:')
