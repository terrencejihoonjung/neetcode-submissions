class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        if (prerequisites.length === 0) return true;

        const prereqs = new Map<number, number[]>();
        for (const [req, prereq] of prerequisites) {;
            if (!prereqs.has(prereq)) prereqs.set(prereq, []);
            prereqs.get(prereq).push(req);
        }

        const seen = new Set<number>();
        const globalSeen = new Set<number>();

        for (let i = 0; i < numCourses; i++) {
            if (globalSeen.has(i)) continue;
            const isValid = this.dfs(i, prereqs, seen, globalSeen);
            if (!isValid) return false;
        }
        return true;
    }

    dfs(course: number, prereqs: Map<number, number[]>, seen: Set<number>, globalSeen: Set<number>): boolean {
        if (globalSeen.has(course)) return true;
        seen.add(course);
        globalSeen.add(course);

        const nextCourses = prereqs.get(course) ?? [];
        let isValid = true;
        for (const next of nextCourses) {
            if (seen.has(next)) return false;
            isValid = isValid && this.dfs(next, prereqs, seen, globalSeen);
        }

        seen.delete(course);

        return isValid;
    }
}

// what entails true? 
// - no circular dependency between courses (cycle)

// 1) transform prerequisites into adjacency list as a map
// 2) for each course in numCourses, perform DFS 
//    - use a global seen that checks for courses we can skip since we visited them alr
//    - use a local seen in each DFS that checks for cycles 
// 3) DFS -> course: number, prereqs map, seen, globalSeen
//    - a) mark as seen, then check global seen.
//    - b) for each next course, perform dfs on courses not seen. If seen, return false. If global seen, no need to run dfs. 
//   - c) return the result of all dfs calls being true or false
