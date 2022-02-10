import os
import sys
from functools import lru_cache
from ansiwrap import ansilen

os.system('color')  # enable ANSI escape characters on windows terminal


class Color:
    colors = {
        # credit: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal#answer-39452138
        'WHITE': '\x1b[1;37;40m',
        'BLUE': '\x1b[1;34;40m',
        'RED': '\x1b[1;31;40m',
        'PURPLE': '\x1b[1;35;40m',
        'END': '\x1b[0m'
    }

    @classmethod
    def this(cls, n):
        return f"{list(cls.colors.values())[cls.color(n)]}{n}{cls.colors['END']}"

    @classmethod
    def color(cls, num):
        """
        0: none
        1: divisible by 2
        2: divisible by 3
        3: both
        """
        return (3 - bool(num % 3) * 2) - num % 2


# return default value if accessed index of array is out of bounds
def get(arr, index, default=0):
    if 0 <= index < len(arr):
        return arr[index]
    return default


# cache last call for calculation in next call
@lru_cache(maxsize=2)
def pascal(n):
    if n == 1:
        return [1]
    return [get(pascal(n-1), k-1) + get(pascal(n-1), k) for k in range(n)]


# center string containing hidden ansi chars
def adjust(s, cols):
    if ansilen(s) > cols:
        return s
    else:
        return f"{((cols - ansilen(s)) // 2) * ' '}{s}"


def render(rows):
    for row in rows:
        string = ' '.join([Color.this(num) for num in row])
        if ansilen(string) <= COLS:
            print(adjust(string, COLS))
        else:
            print("Out of space!".center(COLS))
            break


def main():
    size = int(input("How tall? "))
    rows = [pascal(n) for n in range(1, size+1)]
    render(rows)


COLS, LINES = os.get_terminal_size()

if len(sys.argv) == 2:
    COLS = int(sys.argv[1])

main()
