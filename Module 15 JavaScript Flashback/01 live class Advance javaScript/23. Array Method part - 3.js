//array push()
let fruits = ["apple", "banana", "orange"];
fruits.push("mango"); // adds "mango" to the end of the array   
//output: ["apple", "banana", "orange", "mango"]


//array reverse()
let numbers = [1, 2, 3, 4, 5];
numbers.reverse();
//output: [5, 4, 3, 2, 1]

//array shift()
let f = ["apple", "banana", "orange"];
f.shift(); // removes the first element "apple" from the array
//output: ["banana", "orange"]


//array slice()
let fruits1 = ["apple", "banana", "orange", "mango"];
let slicedFruits = fruits1.slice(1, 3); // extracts elements from index 1 to 2 (not including index 3)
//output: ["banana", "orange"]


//array some() : checks if at least one element in the array passes the test implemented by the provided function.
let numbers1 = [1, 2, 3, 4, 5];
let hasEvenNumber = numbers1.some(function (number) {
    return number % 2 === 0; // checks if the number is even
});
//output: true (since 2 and 4 are even numbers)



//array sort()
let num = [5, 3, 8, 1, 2];
num.sort(function (a, b) {
    return a - b; // sorts the array in ascending order
});
//output: [1, 2, 3, 5, 8]
//for descending order, use b - a


//sort string
let fruits2 = ["banana", "apple", "cherry"];
fruits2.sort(); // sorts the array in alphabetical order
//output: ["apple", "banana", "cherry"]


//array splice()
let fruits3 = ["apple", "banana", "orange", "mango"];
fruits3.splice(2, 1, "kiwi", "grape"); // removes 1 element at index 2 and adds "kiwi" and "grape"
//output: ["apple", "banana", "kiwi", "grape", "mango"]



//array toString()
let fruits4 = ["apple", "banana", "orange"];
let fruitsString = fruits4.toString(); // converts the array to a string
//output: "apple,banana,orange"



//array unshift()
let fruits5 = ["banana", "orange"];
fruits5.unshift("apple"); // adds "apple" to the beginning of the array
//output: ["apple", "banana", "orange"]

