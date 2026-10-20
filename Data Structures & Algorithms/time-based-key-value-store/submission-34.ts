type TimeValue = [number, string]
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
        const timeValues = this.keyStore.get(key);
        if (!timeValues) return "";

        let left = 0;
        let right = timeValues.length - 1;
        let ret = "";
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            const val = timeValues[mid][1];

            if (timeValues[mid][0] <= timestamp) {
                ret = val;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return ret;
    }
}

// store [timestamp, value] pairs under key in array -> Map<string, [number, string]>
// use binary search to find largest pair's timestamp that is less than or equal to timestmap