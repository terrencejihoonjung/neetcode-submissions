class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses: number, prerequisites: number[][]): boolean {
        // map out prerequisites into a graph 
        const courses = new Map<number, number[]>();
        for (const [course, prereq] of prerequisites) {
            if (!courses.has(prereq)) courses.set(prereq, []);
            courses.get(prereq).push(course);
        }

        // iterate through numCourses and perform dfs on each course 
        const globalSeen = new Set<number>();
        const seen = new Set<number>();
        for (let i = 0; i < numCourses; i++) {
            if (!globalSeen.has(i)) {
                const isValid = this.dfs(courses, i, seen, globalSeen);
                if (!isValid) return false;
            }
        }

        return true;
    }

    // dfs returns boolean (true if valid path, false if cycle detected)
    dfs(courses: Map<number, number[]>, course: number, seen: Set<number>, globalSeen: Set<number>): boolean {
        if (seen.has(course)) return false;
        if (globalSeen.has(course)) return true;

        seen.add(course);

        const coursesToTake = courses.get(course) ?? [];
        for (const newCourse of coursesToTake) {
            const isValid = this.dfs(courses, newCourse, seen, globalSeen);
            if (isValid === false) return false;
        }
        
        seen.delete(course);
        globalSeen.add(course);

        return true;
    }
}

// If cycle exists -> we cannot finish courses 
// We should map out prerequisites into a graph 
// - prerequisite class -> classes to take after [] (Map<number, number[]>)

// Iterate through keys of this map and perform DFS
// - for each DFS path, if we detect a cycle -> return false
// - use a set to mark seen courses for each DFS path
// - use a global set to mark seen DFS paths
// - if we encounter a course from the global set in a path, we can early return 