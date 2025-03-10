/**
 * Class: TimeLimitedCache
 * Description: This class allows storing key-value pairs with an expiration time.
 * - `set(key, value, duration)`: Sets a key with a value that expires after `duration` ms. 
 *   If the key already exists and hasn't expired, returns `true`; otherwise, `false`.
 * - `get(key)`: Returns the value if the key exists and hasn't expired, otherwise returns `-1`.
 * - `count()`: Returns the count of unexpired keys in the cache.
 */
class TimeLimitedCache {
    constructor() {
        this.cache = new Map(); // Stores keys with values and expiration timestamps
    }

    /**
     * Sets a key-value pair with a time limit
     * @param {number} key - The key to store
     * @param {number} value - The value to store
     * @param {number} duration - The duration in milliseconds before expiration
     * @return {boolean} - Returns true if key existed before and hasn't expired, otherwise false
     */
    set(key, value, duration) {
        const alreadyExists = this.cache.has(key) && this.cache.get(key).expiration > Date.now();
        const expiration = Date.now() + duration;

        // Store value with its expiration time
        this.cache.set(key, { value, expiration });

        // Set a timeout to delete the key after the expiration time
        setTimeout(() => {
            if (this.cache.get(key)?.expiration === expiration) {
                this.cache.delete(key);
            }
        }, duration);

        return alreadyExists;
    }

    /**
     * Gets the value associated with a key
     * @param {number} key - The key to retrieve
     * @return {number} - The value if key is valid, otherwise -1
     */
    get(key) {
        const entry = this.cache.get(key);
        if (!entry || entry.expiration <= Date.now()) {
            return -1;
        }
        return entry.value;
    }

    /**
     * Counts the number of unexpired keys
     * @return {number} - The number of keys that have not expired
     */
    count() {
        const now = Date.now();
        let count = 0;

        for (const [key, entry] of this.cache) {
            if (entry.expiration > now) {
                count++;
            } else {
                this.cache.delete(key); // Cleanup expired keys
            }
        }
        return count;
    }
}

// Example Test Cases
if (require.main === module) {
    const timeLimitedCache = new TimeLimitedCache();

    console.log(timeLimitedCache.set(1, 42, 100)); // Expected output: false
    console.log(timeLimitedCache.get(1)); // Expected output: 42
    setTimeout(() => console.log(timeLimitedCache.get(1)), 150); // Expected output: -1 (expired)
    
    console.log(timeLimitedCache.set(2, 50, 200)); // Expected output: false
    console.log(timeLimitedCache.set(2, 60, 300)); // Expected output: true (overwrites unexpired key)
    
    setTimeout(() => console.log(timeLimitedCache.count()), 250); // Expected output: 1 (only key=2 exists)
    setTimeout(() => console.log(timeLimitedCache.count()), 350); // Expected output: 0 (all expired)
}

/*

Complexity Analysis:
- Time Complexity:
  - `set()`: O(1) - Stores the key and schedules a timeout.
  - `get()`: O(1) - Retrieves a key and checks expiration.
  - `count()`: O(n) - Iterates through the cache to count valid keys.
- Space Complexity: O(n) - Stores up to `n` keys in the cache.

*/


