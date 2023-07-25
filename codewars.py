# TASK: https://www.codewars.com/kata/53f40dff5f9d31b813000774
def recoverSecret(triplets):
    result = ''
    i = 0
    first = triplets[0][0]
    while triplets:
        if first in triplets[i] and triplets[i][0] != first:
            first = triplets[i][0]
            i = -1
        i += 1
        if i == len(triplets):
            result += first
            for triplet in triplets:
                if first in triplet:
                    triplet.remove(first)
            while [] in triplets:
                triplets.remove([])
            if triplets:
                first = triplets[0][0]
            i = 0

    return result


# TASK: https://www.codewars.com/kata/51b66044bce5799a7f000003
class RomanNumerals:
    @staticmethod
    def to_roman(val):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        result = ''
        for i in range(13):
            if val // values[i]:
                result += val // values[i] * symbols[i]
                val %= values[i]

        return result

    @staticmethod
    def from_roman(roman_num):
        values = [900, 1000, 400, 500, 90, 100, 40, 50, 9, 10, 4, 5, 1]
        symbols = ['CM', 'M', 'CD', 'D', 'XC', 'C', 'XL', 'L', 'IX', 'X', 'IV', 'V', 'I']

        for i in range(13):
            roman_num = roman_num.replace(symbols[i], ' ' + str(values[i]))

        return sum([int(x) for x in roman_num.strip().split(' ')])


# TASK: https://www.codewars.com/kata/54b72c16cd7f5154e9000457
def decode_bits(bits):
    bits = bits.strip('0')
    seq = 1
    unit = 0
    if len(bits) > 1:
        for i in range(1, len(bits)):
            if bits[i - 1] == bits[i]:
                seq += 1
            elif bits[i - 1] != bits[i] and not unit:
                unit = seq
                seq = 1
            else:
                unit = min(unit, seq)
                seq = 1
        if not unit:
            unit = seq

        bits = ''.join([x for i, x in enumerate(bits) if not i % unit])

    return bits.replace('0000000', '   ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')


def decode_morse(morseCode):
    words = morseCode.strip().split('   ')
    result = ''
    for index, word in enumerate(words):
        if index > 0:
            result += ' '
        for letter in word.split(' '):
            result += MORSE_CODE[letter]

    return result


# TASK: https://www.codewars.com/kata/54b724efac3d5402db00065e
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip()
    words = morse_code.split('   ')
    result = ''
    for index, word in enumerate(words):
        if index > 0:
            result += ' '
        for letter in word.split(' '):
            result += MORSE_CODE[letter]

    return result


# TASK: https://www.codewars.com/kata/540afbe2dc9f615d5e000425
class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        n = len(self.data)
        srn = int(n ** 0.5)
        squares, columns = [], []

        if n == 1 and str(self.data[0][0]) == 'True':
            return False

        for row in self.data:
            if len(row) != n:
                return False

        for i in range(n):
            square = []
            for x in range(srn):
                for y in range(srn):
                    square.append(self.data[(i % srn) * srn + x][(i // srn) * srn + y])
            squares.append(square)

        for x in range(n):
            column = []
            for y in range(n):
                column.append(self.data[y][x])
            columns.append(column)

        for i in range(n):
            for j in range(1, n + 1):
                if self.data[i].count(j) != 1:
                    return False
                if squares[i].count(j) != 1:
                    return False
                if columns[i].count(j) != 1:
                    return False

        return True


# TASK: https://www.codewars.com/kata/5324945e2ece5e1f32000370
import itertools


def sum_strings(x, y):
    x = '0' + x
    y = '0' + y
    sums = [sum(int(j) for j in i) for i in itertools.zip_longest(list(x[::-1]), list(y[::-1]), fillvalue='0')][::-1]
    for i in range(len(sums) - 1, -1, -1):
        if sums[i] > 9:
            sums[i - 1] += sums[i] // 10
            sums[i] = sums[i] % 10
    sums = ''.join(str(i) for i in sums)
    while len(sums) > 1 and sums[0] == '0':
        sums = sums[1:]

    return sums if sums != '' else '0'


# TASK: https://www.codewars.com/kata/5263c6999e0f40dee200059d
from itertools import product

def get_pins(observed):
    dict = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [5, 7, 8, 9, 0],
        9: [6, 8, 9],
        0: [0, 8],
    }
    list_of_nums = [dict[int(x)] for x in observed]
    return [''.join([str(y) for y in x]) for x in list(product(*list_of_nums))]


# TASK: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    res = [str(args[0])]
    count = 1
    for i in range(1, len(args)):
        if args[i - 1] == args[i] - 1:
            count += 1
        else:
            count = 1

        if count < 3:
            res.append(',' + str(args[i]))
        else:
            res.pop(-1)
            res.append('-' + str(args[i]))

    return ''.join(res)


# TASK: https://www.codewars.com/kata/550f22f4d758534c1100025a
def dirReduc(arr):
    vec = {
        "NORTH": [0, 1],
        "SOUTH": [0, -1],
        "EAST": [1, 0],
        "WEST": [-1, 0],
    }
    dir = []
    for i in range(len(arr)):
        if not len(dir):
            dir.append(arr[i])
        elif [sum(v) for v in zip(vec[arr[i]], vec[dir[-1]])] == [0, 0]:
            dir.pop(-1)
        else:
            dir.append(arr[i])

    return dir


# TASK: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(sm):
    result = []
    while len(sm)>0:
        n=len(sm)
        if len(sm[0]):
            for i in range(n):
                result.append(sm[0].pop(0))
        if n>2:
            for i in range(1, n-1):
                result.append(sm[i].pop(n-1))
        if n>1:
            for i in range(n-1, -1, -1):
                result.append(sm[n-1].pop(i))
        if n>2:
            for i in range(n-2, 0, -1):
                result.append(sm[i].pop(0))
        if n>1:
            sm.pop(n-1)
        sm.pop(0)
    return result


# TASK: https://www.codewars.com/kata/55983863da40caa2c900004e
# SIMPLE SOLUTION THAT WORKS FOR SMALL NUMBERS
# from itertools import permutations

# def next_bigger(n):
#     p = [int(''.join(x)) for x in list(permutations(str(n), len(str(n)))) if int(''.join(x))>n]
#     return min(p) if len(p) else -1
def next_bigger(n):
    rev = list(str(n)[::-1])
    end = []
    found = False
    while len(rev) > 1 and not found:
        if rev[0] > rev[1]:
            x = rev[1]
            end.append(rev.pop(0))
            end.append(rev.pop(0))
            connector = min([y for y in end if y > x])
            end.pop(end.index(connector))
            found = True
        else:
            end.append(rev.pop(0))
    rev.reverse()
    end.sort()
    return int(''.join(rev) + connector + ''.join(end)) if found else -1


# TASK: https://www.codewars.com/kata/526571aae218b8ee490006f4
def count_bits(n):
    return sum([int(a) for a in "{:b}".format(n)])


# TASK: https://www.codewars.com/kata/513e08acc600c94f01000001
def rgb(r, g, b):
    rgb=[r, g, b]
    for i, x in enumerate(rgb):
        if x<0:
            rgb[i]=0
        elif x>255:
            rgb[i]=255
        print(x)
    return ''.join([hex(x)[2:].upper() if len(hex(x)[2:])==2 else '0'+hex(x)[2:].upper() for x in rgb])


# TASK: https://www.codewars.com/kata/52597aa56021e91c93000cb0
def move_zeros(lst):
    zeros = 0
    try:
        while 1:
            lst.remove(0)
            zeros+=1
    except:
        for i in range(zeros):
            lst.append(0)
    return lst


# TASK: https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    return [x for x in seq if seq.count(x)%2][0]


# TASK: https://www.codewars.com/kata/5264d2b162488dc400000001
def spin_words(sentence):
    words = []
    try:
        while sentence.index(' '):
            words.append(sentence[:sentence.index(' ')])
            sentence = sentence[(sentence.index(' ') + 1):]
    except:
        words.append(sentence)
        sentence = ''
        for index, word in enumerate(words):
            if len(word) > 4:
                words[index] = word[::-1]

        sentence = ' '.join(words)

    return sentence


# TASK: https://www.codewars.com/kata/541c8630095125aba6000c00
def digital_root(n):
    while n>9:
        sum = 0
        for sign in str(n):
            sum += int(sign)
        n = sum
    return n


# TASK: https://www.codewars.com/kata/568fca718404ad457c000033
def find(seq):
    seq.sort()
    return (seq[0]+seq[-1])/2*(len(seq)+1) - sum(seq)