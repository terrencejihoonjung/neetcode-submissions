class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find the smaller list 
        l1, l2 = nums1, nums2
        if len(l2) < len(l1): 
            l1, l2 = l2, l1

        # calculate the half-length of size(nums1 + nums2) 
        size = len(l1) + len(l2)
        half = size // 2

        # begin partitioning process 
        l = 0
        r = len(l1) - 1

        while True:
            mid1 = (l + r) // 2
            mid2 = half - (mid1 + 1) - 1 # because both nums1 and nums2 are 0-indexed

            num1 = l1[mid1] if mid1 >= 0 else float("-infinity")
            num2 = l2[mid2] if mid2 >= 0 else float("-infinity")
            next_num1 = l1[mid1 + 1] if (mid1 + 1) < len(l1) else float("infinity")
            next_num2 = l2[mid2 + 1] if (mid2 + 1) < len(l2) else float("infinity")

            if num1 <= next_num2 and num2 <= next_num1:
                if size % 2 == 0:
                    return (min(next_num1, next_num2) + max(num1, num2)) / 2
                else:
                    return min(next_num1, next_num2)
            
            if num1 > next_num2:
                r = mid1 - 1
            else:
                l = mid1 + 1

# arrays are sorted in ascending order
# arrays have differing sizes 
# O(log(m + n)) points to a binary search algorithm where the input space includes both arrays 
# - some sort of simultaneous binary search on nums1 and nums2

# how to find median? -> the median if considering both nums1 and nums2 can be found 
#                        if the left and right partition are of equal size

# we really only need to focus on one of the partitions since we know:
# - (len(nums1) + len(nums2)) // 2

# since we know the arrays are in ascending order we can build the left partition using the 
# left-most elements in nums1 and nums2

# let's take half of the elements in nums1. 
# then the remaining half to take is half - nums1_half
# - this remaining half will be taken from nums2

# at this point, we should correct the numerical ordering if needed. Check if the nums1 right-most element is less than or equal to nums right-most element + 1. Then vice versa. 
# If the condition checks out, we have the left partition! so we should calculate the median based on the full lneght (even or odd) 

# if the conditions don't check out, we need to udpate pointers. 
# - if nums1's right most pointer is greater, then right = mid - 1. if nums2's right most pointer is greater, then left = mid + 1

# we should also start with the smaller array since we might take more than half if we go with the larger array