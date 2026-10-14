class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const prefix = new Array<number>(nums.length);
        prefix[0] = 1;
        for (let i = 1; i < nums.length; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        let sProd = 1
        for (let i = nums.length - 1; i >= 0; i--) {
            prefix[i] *= sProd;
            sProd *= nums[i]
        }

        return prefix
    }
}

// Brute force
// - for each num in nums, multiple the other nums 
// - time/space: O(n^2)/O(n)

// Optimized w/o division
// - use prefix and suffix product arrays to find product excluding num at each index 
// - time/space: O(n)

// Optimized w/o division and using just prefix product array
// - build prefix product array
// - iterate backwards on nums and build suffix product. Along the way, add the accumulating product 
//   to the num at the current index of the prefix prod array. Finally, return the prefix array
// - time/space: O(n)