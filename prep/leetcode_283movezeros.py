

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    zc = nums.count(0)

    for i in range(zc):
        for idx, num in enumerate(nums):
            if num == 0 and idx+1 < len(nums):
                print(idx)
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
    return nums

def test_ex1():
    nums = [0, 1, 0, 3, 12]

    assert moveZeroes(nums) == [1, 3, 12, 0, 0]


def test_edgecase():
    nums = []

    assert moveZeroes(nums) == []