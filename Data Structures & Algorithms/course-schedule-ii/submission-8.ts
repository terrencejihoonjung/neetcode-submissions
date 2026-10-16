class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses: number, prerequisites: number[][]): number[] {
        const courses = new Map<number, number[]>();
        const indegrees = new Map<number, number>();

        for (const [c, p] of prerequisites) {
            if (!courses.has(p)) courses.set(p, []);
            courses.get(p).push(c);
            
            indegrees.set(c, (indegrees.get(c) ?? 0) + 1);
        }

        for (let i = 0; i < numCourses; i++) {
            if (!indegrees.has(i)) {
                indegrees.set(i, 0);
            }
        }

        const queue: number[] = [];
        for (const [k, v] of indegrees.entries()) {
            if (v === 0) queue.push(k);
        }

        let head = 0;
        const ret: number[] = [];
        const seen = new Set<number>();

        while (head < queue.length) {
            const course = queue[head++];
            ret.push(course); 
            seen.add(course);

            const nextCourses = courses.get(course) ?? [];
            for (const next of nextCourses) {
                if (seen.has(next)) return [];

                indegrees.set(next, indegrees.get(next) - 1);
                if (indegrees.get(next) === 0) {
                    queue.push(next);
                }
            }
        }

        if (head !== numCourses) return [];

        return ret;
    }
}

// We want to take the courses that don't have prereqs first 
// Then take the courses that are takeable after we take those intiial courses 

// This sounds like we need to find a topological ordering of these classes 
// Use Kahn's algorithm

// Create mapping of prereqs to courses + get indegrees of each course

// Initialize a queue with the courses that have 0 indegrees

// Iterate through queue while it is non-empty. Use head pointer to avoid O(n) shift
// For each iteration, we add course to ret + move head pointer, then check if any of its next courses has a resulting indegree of 0 -> enqueue
// use seen to track visisted courses 

// At the end, if head pointer !== numCourses, we encountered a cycle -> return []
// else return ret
