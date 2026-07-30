class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A 
        
        full = len(A) + len(B)
        half = full // 2

        l, r = 0, len(A) - 1
        while True:
            mid = (l + r) // 2
            remaining = half - (mid + 1) - 1

            a_left = A[mid] if mid >= 0 else float("-infinity")
            a_right = A[mid + 1] if (mid + 1) < len(A) else float("infinity")
            b_left = B[remaining] if remaining >= 0 else float("-infinity")
            b_right = B[remaining + 1] if (remaining + 1) < len(B) else float("infinity")

            if a_left <= b_right and b_left <= a_right: 
                if full % 2 == 0:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
                else:
                    return min(a_right, b_right)
            
            elif a_left > b_right: 
                r = mid - 1
            else:
                l = mid + 1

