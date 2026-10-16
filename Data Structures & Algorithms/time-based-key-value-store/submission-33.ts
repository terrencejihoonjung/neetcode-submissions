type TimeValue = [number, string];

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
        const times = this.keyStore.get(key);
        if (!times) return "";

        let l = 0; 
        let r = times.length - 1;
        let res = "";
        while (l <= r) {
            const mid = Math.floor((l + r) / 2);
            const time = times[mid][0];

            if (time <= timestamp) {
                res = times[mid][1];
                l = mid + 1;
            }

            else {
                r = mid - 1;
            }
        }

        return res;
    }
}

// map key -> [timestamp, value][]

// set: add to map (naturally chronological order)
// get: get timestamp value pairs using key. run binary search to find exact match or next largest before it 