// Array Methods Examples

// 1. Array from(): used to create a new array instance from an array-like or iterable object
const arrFrom = Array.from('hello');
console.log("Array.from():", arrFrom); // Output: ['h', 'e', 'l', 'l', 'o']

// 2. Array includes()
const arrIncludes = [1, 2, 3, 4, 5];
console.log("Array.includes():", arrIncludes.includes(3)); // Output: true

// 3. Array join()
const arrJoin = ['a', 'b', 'c'];
console.log("Array.join():", arrJoin.join('-')); // Output: "a-b-c"


// 4. Array lastIndexOf(): used to return the last index at which a given element can be found in the array, or -1 if it is not present
const arrLastIndexOf = [1, 2, 3, 2, 1];
console.log("Array.lastIndexOf():", arrLastIndexOf.lastIndexOf(2)); // Output: 3

// 5. Array length
const arrLength = [10, 20, 30];
console.log("Array.length:", arrLength.length); // Output: 3

// 6. Array pop()
const arrPop = [1, 2, 3];
const poppedElement = arrPop.pop();
console.log("Array.pop():", poppedElement, arrPop); // Output: 3 [1, 2]
