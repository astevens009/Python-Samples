def solution1(nums, k):
    """Return the kth largest number using slicing

    Args:
        nums (list): unsorted sequence
        k (int): kth largest element to find

    Returns:
        int: kth largest element
    """
    nums.sort()

    print("\nTEST - sorted list: {}\n".format(nums))
    print("\nTEST: solution 1")

    return nums[-k]

def solution2(nums, k):
    """Return the kth largest element using the length of the array

    Args:
        nums (list): unsorted sequence
        k (int): kth largest element to find
    """
    nums.sort()

    print("\nTEST - sorted list: {}\n".format(nums))
    print("\nTEST: solution 2")

    return nums[len(nums) - k]

# k = 2
k = int(input("\nPlease enter a number: "))
nums = [3,2,1,5,6,4]
nums2 = [3,2,3,1,2,4,5,5,6]

if 0 < k < len(nums):
    kthLargest = solution1(nums, k)
    print("The {}th largest number in the array\n\n{}\n\nis {}\n".format(k, nums, kthLargest))
    
    kthLargest = solution1(nums2, k)
    print("The {}th largest number in the array\n\n{}\n\nis {}\n".format(k, nums2, kthLargest))

    kthLargest = solution2(nums, k)
    print("The {}th largest number in the array\n\n{}\n\nis {}\n".format(k, nums, kthLargest))
    
    kthLargest = solution2(nums2, k)
    print("The {}th largest number in the array\n\n{}\n\nis {}\n".format(k, nums2, kthLargest))
else:
    print("Invalid input or not enough elements in the array.\n")
