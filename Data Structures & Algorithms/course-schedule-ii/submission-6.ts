class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses: number, prerequisites: number[][]): number[] {
        if (numCourses === 1) return [0];

        const reqs = new Map<number, number[]>();
        const indegrees = new Map<number, number>();
        for (const [c, p] of prerequisites) {
            if (!reqs.has(p)) reqs.set(p, []);
            reqs.get(p).push(c);
            indegrees.set(c, (indegrees.get(c) ?? 0) + 1);
        }

        for (let i = 0; i < numCourses; i++) {
            if (!indegrees.has(i)) {
                indegrees.set(i, 0);
            }
        }

        const queue: number[] = [];
        for (const [key, val] of indegrees.entries()) {
            if (val === 0) {
                queue.push(key);
            }
        }

        const ret: number[] = [];
        let head: number = 0;

        while (head < queue.length) {
            const course = queue[head++];
            ret.push(course);

            const nextCourses = reqs.get(course) ?? [];
            for (const next of nextCourses) {
                
                indegrees.set(next, indegrees.get(next) - 1)
                if (indegrees.get(next) === 0) {
                    queue.push(next);
                }
            }
        }
        
        if (head != numCourses) return [];

        return ret;
    }
}

// Use Kahn's algorihtm to get a topological ordering of the courses 

// 1) Map prereqs to courses + map each course to their indegree 
// 2) For each course with indegree === 0, add to a queue 
// 3) Iterate through queue:
//    - enqueue when the updated indegree of a prereq's courses become 0
//    - use head pointer to simulate an enqueue
//    - cycle detection? -> use a set since courses are unique -> early return