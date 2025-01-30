"""
File: Kth_array.py
Name: Jennifer Li
------------------------
TODO:
"""
import heapq


def find_kth_largest(nums, k):
    """
    Given a nums list and k, this function will return Kth largest element in nums
    Even if nums have same number, they still need to be sort and ranked.

    Input:
        nums (list): a list with integer
        k (int): Kth largest element

    Returns:
        kth_largest (int): Kth largest element in nums
    """
    print(f'The {k}th largest element in {nums} is ', end='')
    # ----- YOUR CODE STARTS HERE ----- #
    heapq.heapify(nums)
    for i in range(len(nums)-k):
        heapq.heappop(nums)
    return nums[0]

    # Using the MaxHeap solution
    # heapq.heapify(nums)
    # for i in range(len(nums)):
    #     nums[i] = -nums[i]
    # heapq.heapify(nums)
    # for i in range(k-1):
    #     heapq.heappop(nums)
    # for i in range(len(nums)):
    #     nums[i] = -nums[i]
    # return nums[0]


def main():
    print(find_kth_largest([4], 1))
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(find_kth_largest([1, 5, 3, 8, 3], 2))


if __name__ == '__main__':
    main()
