type TimeValue = [number, string] | [];

class TimeMap {
    keyStore: Map<string, TimeValue[]>;

    constructor() {
        this.keyStore = new Map<string, TimeValue[]>();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key: string, value: string, timestamp: number): void {
        if (!this.keyStore.has(key)) this.keyStore.set(key, []);
        this.keyStore.get(key).push([timestamp, value]);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key: string, timestamp: number): string {
        const vals = this.keyStore.get(key);
        if (!vals) return "";

        let left = 0;
        let right = vals.length - 1;

        if (timestamp < vals[left][0]) return "";
        if (timestamp > vals[right][0]) return vals[right][1];

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            const time = vals[mid][0];
            const val = vals[mid][1];

            if (time === timestamp) return val;

            else if (time < timestamp) {
                left = mid + 1;
            }

            else {
                right = mid - 1;
            }
        }
        return vals[right][1];
    }
}

// store data -> map<string, number[][]> 
// - key is numeric key
// - value is [time, val]
// This allows us to store multiple values on the same key at different timestamps

// timestamps being strictly increasing on set calls means that the map values are in chronological order -> makes binary search possible -> get can be O(logn)

