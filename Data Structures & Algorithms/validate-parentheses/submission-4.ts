class Solution {

    parantheses = new Map<string, string>([["(", ")"], ["[", "]"], ["{", "}"]])

    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const stack = new Array<string>()
        for (const c of s) {
            if (this.parantheses.has(c)) {
                stack.push(this.parantheses.get(c))
            }

            else {
                if (stack.length === 0) return false

                const popped = stack.pop()
                if (popped !== c) return false
            }
        }

        return stack.length === 0

    }
}
