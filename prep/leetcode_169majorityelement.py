import pytest


def majorityElement(nums):
    '''
    Find the majority element that appears > n/2
    where n = size of array

    :type nums: List[int]
    :rtype: int

    '''

    nums_dict = {}
    nums_max = nums[0]

    for num in nums:
        if num in nums_dict.keys():
            nums_dict[num] +=1
        else:
            nums_dict[num] = 1

        if nums_dict[num] > nums_dict[nums_max]:
            nums_max = num

    return nums_max


def test_base():
    nums = [0, 1, 2, 3, 3, 3, 3]
    assert majorityElement(nums) == 3


def test_base():
    nums = [6, 5, 5]
    assert majorityElement(nums) == 5