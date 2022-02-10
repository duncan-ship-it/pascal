import os
from functools import lru_cache
import ansiwrap

os.system('color')  # enable ANSI escape characters on windows terminal


"""
Very Hard: Use a language/format that allows the colouring of letters (most console outputs should allow this) and make 
any number divisible by 2 blue, and any number divisible by 3 red, any number divisible by both purple.
"""


class Color:
    colors = {
        # credit: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal#answer-39452138
        'WHITE': '\x1b[1;37;40m',
        'RED': '\x1b[1;34;40m',
        'BLUE': '\x1b[1;32;40m',
        'GREEN': '\x1b[1;31;40m',
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


@lru_cache(maxsize=2)
def pascal(n):
    if n == 1:
        return [1]
    return [get(pascal(n-1), k-1) + get(pascal(n-1), k) for k in range(n)]


# center string containing ansi chars given width
def adjust(s, cols):
    if ansiwrap.ansilen(s) > cols:
        return s
    else:
        return f"{((cols-ansiwrap.ansilen(s))//2 + 1)*' '}{s}"


def render(rows, len_lim=8):
    width = min(len(str(max(rows[-1]))), len_lim)  # max width of each number

    for row in rows:
        string = ' '.join([adjust(Color.this(num), width) for num in row])
        print(adjust(string, COLS))


def main():
    size = int(input("How tall? "))
    rows = [pascal(n) for n in range(1, size+1)]
    render(rows, len_lim=16)


LINES, COLS = os.get_terminal_size()

if COLS > 200:
    COLS = 7000  # must be in actual terminal, can be much more

main()
