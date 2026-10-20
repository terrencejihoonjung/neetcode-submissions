class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target: number, position: number[], speed: number[]): number {
        const cars: number[][] = [];
        for (let i = 0; i < position.length; i++) {
            cars.push([position[i], speed[i]]);
        }

        cars.sort((a, b) => a[0] - b[0]);

        const times: number[] = [];
        for (const [pos, spd] of cars) {
            let time = (target - pos) / spd; 

            while (times.length > 0 && time >= times[times.length - 1]) {
                const popped = times.pop();
                time = Math.max(popped, time);
            }

            times.push(time);
        }
        return times.length;
    }
}

// given target, position, and speed we can calculate the # of steps it takes to get to target for a given car 
// group position/speed into one array, sort by position to get an ordering of cars

// maintain a stack of times and merge cars that become car fleets
// what calls for a merge? -> when the calculated steps of the current car is greater than or equal to the car at the top of the stack 
// what do we do at a merge? -> add the larger time of the two 

// return the length of the stack