/**
 * Function: findMin
 * Description: Given a rotated sorted array of unique elements, this function finds
 * the minimum element in O(log n) time using binary search.
 *
 * @param {number[]} nums - A rotated sorted array of unique integers.
 * @returns {number} - The minimum element in the array.
 */
const findMin = function(nums) {
    let left = 0, right = nums.length - 1;

    while (left < right) {
        let mid = Math.floor((left + right) / 2);

        // If mid element is greater than the rightmost element, min must be in the right half
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // If mid element is smaller than the rightmost, the minimum could be mid or to the left
            right = mid;
        }
    }

    return nums[left]; // Left now points to the minimum element
};

// Example Test Cases
if (require.main === module) {
    console.log("Test 1: Basic rotated array");
    console.log(findMin([3,4,5,1,2]));
    // Expected output: 1

    console.log("Test 2: Larger rotated array");
    console.log(findMin([4,5,6,7,0,1,2]));
    // Expected output: 0

    console.log("Test 3: Already sorted array (no rotation)");
    console.log(findMin([11,13,15,17]));
    // Expected output: 11

    console.log("Test 4: Rotated at one element");
    console.log(findMin([2,3,4,5,6,7,8,1]));
    // Expected output: 1

    console.log("Test 5: Two-element rotated array");
    console.log(findMin([2,1]));
    // Expected output: 1

    console.log("Test 6: Single-element array");
    console.log(findMin([7]));
    // Expected output: 7
}

/*
Time Complexity: O(log n) - Binary search halves the search space at each step.
Space Complexity: O(1) - Only uses constant extra space.
*/

export default findMin;
