import pytest


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    
    return list(map(int, list('{0:32b}'.format(n).replace(' ', '')))).count(1)


def test_base():
    assert hammingWeight(11) == 3