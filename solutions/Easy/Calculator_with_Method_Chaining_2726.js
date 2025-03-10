class Calculator {
    /** 
     * Constructor initializes the calculator with an initial value.
     * @param {number} value - The initial value of the calculator.
     */
    constructor(value) {
        this.result = value;
    }
    
    /** 
     * Function: add
     * Description: Adds the given value to the result.
     * @param {number} value - The number to add.
     * @return {Calculator} - Returns the calculator instance for chaining.
     */
    add(value) {
        this.result += value;
        return this;
    }
    
    /** 
     * Function: subtract
     * Description: Subtracts the given value from the result.
     * @param {number} value - The number to subtract.
     * @return {Calculator} - Returns the calculator instance for chaining.
     */
    subtract(value) {
        this.result -= value;
        return this;
    }
    
    /** 
     * Function: multiply
     * Description: Multiplies the result by the given value.
     * @param {number} value - The number to multiply.
     * @return {Calculator} - Returns the calculator instance for chaining.
     */  
    multiply(value) {
        this.result *= value;
        return this;
    }
    
    /** 
     * Function: divide
     * Description: Divides the result by the given value. Throws an error if dividing by zero.
     * @param {number} value - The number to divide by.
     * @return {Calculator} - Returns the calculator instance for chaining.
     * @throws {Error} - Throws "Division by zero is not allowed" if value is 0.
     */
    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }
        this.result /= value;
        return this;
    }
    
    /** 
     * Function: power
     * Description: Raises the result to the power of the given value.
     * @param {number} value - The exponent.
     * @return {Calculator} - Returns the calculator instance for chaining.
     */
    power(value) {
        this.result = Math.pow(this.result, value);
        return this;
    }
    
    /** 
     * Function: getResult
     * Description: Returns the current result of the calculator.
     * @return {number} - The current calculated result.
     */
    getResult() {
        return this.result;
    }
}

// Example Test Cases
if (require.main === module) {
    try {
        console.log(new Calculator(10).add(5).subtract(7).getResult());
        // Expected output: 8

        console.log(new Calculator(2).multiply(5).power(2).getResult());
        // Expected output: 100

        console.log(new Calculator(20).divide(2).getResult());
        // Expected output: 10

        console.log(new Calculator(3).power(3).getResult());
        // Expected output: 27

        console.log(new Calculator(100).subtract(50).add(25).divide(5).getResult());
        // Expected output: 15

        console.log(new Calculator(50).multiply(2).add(10).subtract(20).divide(4).getResult());
        // Expected output: 20

        console.log(new Calculator(20).divide(0).getResult()); 
        // Expected output: Error "Division by zero is not allowed"

    } catch (error) {
        console.error(error.message);
    }
}

/*

Complexity Analysis:
- Time Complexity:
  - All methods execute in O(1) time as they perform constant time arithmetic operations.
- Space Complexity: O(1) since the result is stored in a single variable.

*/

export default Calculator;
