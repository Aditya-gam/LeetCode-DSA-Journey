class EventEmitter {
    constructor() {
        this.events = new Map();
    }

    /**
     * Function: subscribe
     * Description: Subscribes a callback function to an event.
     * - Multiple callbacks can be added for the same event.
     * - Returns an object with an `unsubscribe` method to remove the callback.
     *
     * @param {string} eventName - The name of the event.
     * @param {Function} callback - The function to be called when the event is emitted.
     * @return {Object} - An object with an `unsubscribe` method.
     */
    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, []);
        }

        this.events.get(eventName).push(callback);

        return {
            unsubscribe: () => {
                this.events.set(eventName, this.events.get(eventName).filter(fn => fn !== callback));
            }
        };
    }

    /**
     * Function: emit
     * Description: Emits an event, invoking all subscribed callbacks in order.
     * - If no listeners are subscribed, returns an empty array.
     *
     * @param {string} eventName - The event to emit.
     * @param {Array} args - Arguments to pass to the event callbacks.
     * @return {Array} - Array of results from invoked callbacks.
     */
    emit(eventName, args = []) {
        if (!this.events.has(eventName)) return [];
        return this.events.get(eventName).map(fn => fn(...args));
    }
}

// Example Test Cases
if (require.main === module) {
    const emitter = new EventEmitter();

    // Test Case 1: Emitting before subscribing
    console.log(emitter.emit("firstEvent")); 
    // Expected output: []

    // Test Case 2: Subscribe to an event
    const sub1 = emitter.subscribe("firstEvent", () => 5);
    console.log(emitter.emit("firstEvent")); 
    // Expected output: [5]

    // Test Case 3: Subscribe another callback
    const sub2 = emitter.subscribe("firstEvent", () => 6);
    console.log(emitter.emit("firstEvent")); 
    // Expected output: [5, 6]

    // Test Case 4: Unsubscribe one listener
    sub1.unsubscribe();
    console.log(emitter.emit("firstEvent")); 
    // Expected output: [6]

    // Test Case 5: Subscribe a callback that takes arguments
    const sub3 = emitter.subscribe("dataEvent", (...args) => args.join(','));
    console.log(emitter.emit("dataEvent", [1, 2, 3])); 
    // Expected output: ["1,2,3"]

    // Test Case 6: Unsubscribe all and emit again
    sub2.unsubscribe();
    sub3.unsubscribe();
    console.log(emitter.emit("firstEvent")); 
    // Expected output: []
}

/*

Complexity Analysis:
- Time Complexity:
  - `subscribe()`: O(1) - Inserts the callback into a map.
  - `emit()`: O(k) - Calls `k` callbacks in order.
  - `unsubscribe()`: O(k) - Filters the list of callbacks.
- Space Complexity: O(n) - Stores `n` callbacks in the event map.

*/

export default EventEmitter;
