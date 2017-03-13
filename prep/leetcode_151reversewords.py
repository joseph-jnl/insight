import pytest


def reverseWords(s):
    '''
    :type s: str
    rtype: str

    Reverse string word by word
    '''

    # stack = []
    rlist = s.split()

    # for word in rlist:
    #     stack.append(word)

    return ' '.join(rlist[::-1])


def test_sky():
    s = "the sky is blue"
    assert reverseWords(s) == 'blue is sky the'