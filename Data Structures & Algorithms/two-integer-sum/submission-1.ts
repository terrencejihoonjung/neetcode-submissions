class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const complements = new Map<number, number>() 
        for (let i: number = 0; i < nums.length; i++) {
            const num = nums[i]
            const complement = target - num 

            if (complements.has(complement)) {
                return [complements.get(complement), i]
            }

            complements.set(num, i)
        }

        return [-1, -1]
    }
}
