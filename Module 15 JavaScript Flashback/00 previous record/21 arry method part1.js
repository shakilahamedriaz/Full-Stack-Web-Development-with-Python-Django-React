//array at()
const arr = [1, 2, 3, 4, 5];
console.log(arr.at(2));
//output: 3


//array concat() : used to merge two or more arrays
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const arr3 = arr1.concat(arr2);
console.log(arr3);
//output: [1, 2, 3, 4, 5, 6]


//array every() : used to test whether all elements in the array pass the test implemented by the provided function
const arr4 = [1, 2, 3, 4, 5];
const isEven = (element) => element % 2 === 0;
const result = arr4.every(isEven);
console.log(result);
//output: false (because not all elements are even)



//array filter() : means to filter the elements of an array based on a condition
const arr5 = [1, 2, 3, 4, 5];

const res =  arr5.filter((element) => num %2 == 0);
console.log(res);
//output: [2, 4] (only even numbers are filtered out)



//array find() : means to find the first element in the array that satisfies the provided testing function
const arr6 = [1, 2, 3, 4, 5];
const findElement = arr6.find((element) => element > 3);
console.log(findElement);
//output: 4 (first element greater than 3)


//array findIndex() : means to find the index of the first element in the array that satisfies the provided testing function
const arr7 = [1, 2, 3, 4, 5];  
const findIndex = arr7.findIndex((element) => element > 3);
console.log(findIndex);
//output: 3 (index of the first element greater than 3)
