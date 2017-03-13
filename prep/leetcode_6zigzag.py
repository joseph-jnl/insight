import numpy as np
from math import ceil


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str


    Construct string array, size(numRows, ceil(len(s) / numRows))

    Fill in array by column
        first column = numrows characters
            then (numrows-2) columns have spaces + 1 character
                character in row numrow-1-i
        then column = numrows characters
        repeat until end
    """

    # Edge cases
    if s == '':
        return ''

    if numRows == 1:
        return s

    # Construct empty array
    numColumns = ceil(len(s) / (numRows + (numRows - 2))) + \
        (ceil(len(s) / (numRows + (numRows - 2))) - 1) * (numRows - 2)

    zarr = np.empty([numRows, numColumns], dtype=str)
    c_count = 0
    diag_count = numRows - 2
    s_padded = s + '                           '

    # Fill in column by column
    for col in range(0, zarr.shape[1]):
        if (col == 0) | (col % (numRows - 1) == 0):
            for row in range(0, numRows):
                zarr[row, col] = s_padded[c_count]
                c_count += 1
        else:
            if numRows == 3:
                zarr[1, col] = s_padded[c_count]
            elif diag_count == 1:
                zarr[1, col] = s_padded[c_count]
                diag_count = numRows - 2
            else:
                zarr[numRows-diag_count, col] = s_padded[c_count]
                diag_count -= 1
            c_count += 1

    # print(zarr)

    # Concat rows into single string
    zigzag = ''
    for row in range(0, numRows):
        zigzag += ''.join(zarr[row, :])

    return zigzag.replace(' ', '')


def test_row3():
    '''
    PAYPALISHIRING 14

    3:
    P   A   H   N
    A P L S I I G
    Y   I   R

    0 4 8 12
    1 3 5 7 9 11 13
    2 6 10

    (3-1) 

    PAHNAPLSIIGYIR
    '''

    s = 'PAYPALISHIRING'
    n = 3
    assert convert(s, n) == 'PAHNAPLSIIGYIR'


def test_row4():
    '''
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    0 6 12
    1 5 7 11 13
    2 4 8 10
    3 9

    4 - 1    

    PINALSIGYAHRPI
    '''

    s = 'PAYPALISHIRING'
    n = 4
    assert convert(s, n) == 'PINALSIGYAHRPI'


def test_row3_ABC():
    '''
    P   A   H   N   C
    A P L S I I G B
    Y   I   R   A
    '''
    s = 'PAYPALISHIRINGABC'
    n = 3
    assert convert(s, n) == 'PAHNCAPLSIIGBYIRA'


def test_null():
    '''
    P   A   H   N   C
    A P L S I I G B
    Y   I   R   A
    '''
    s = ''
    n = 1
    assert convert(s, n) == ''


def test_row1():
    '''
    P   A   H   N   C
    A P L S I I G B
    Y   I   R   A
    '''
    s = 'A'
    n = 1
    assert convert(s, n) == 'A'