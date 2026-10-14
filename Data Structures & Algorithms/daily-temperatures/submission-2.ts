class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        if (temperatures.length === 1) return [0];

        const stack: number[] = [];
        const res: number[] = Array.from({length: temperatures.length}, () => 0)
        
        for (let i = 0; i < temperatures.length; i++) {
            const temp = temperatures[i];
            
            while (stack.length > 0 && temperatures[stack[stack.length - 1]] < temp) {
                const popped = stack.pop()
                res[popped] = i - popped
            }

            stack.push(i)
        }

        return res
    }
}
