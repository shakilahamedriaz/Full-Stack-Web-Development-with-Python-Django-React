//printing hello world in js
console.log("Hello World");
console.log("hello duniya!!");

//variable declaration 
let x = 5;
console.log(`hey there!! ${x}`); // fixed string interpolation

//single line comment:
//how can i check my pretter is working or not

//multi line comment:

/*
console.log("hey there!! {x}");
console.log("hey there!! {x}");
console.log("hey there!! {x}");
*/

let y = 10;
let z = 20;

let sum = x + y + z;
console.log("sum is : ", sum);


let a = 10;
var b = 20;
b = 30; // redeclaring var is allowed

console.log(a); // 10
console.log(b); // 30

var c;
console.log(c); // undefined
c = 10;
console.log(c); // 10

//var:
console.log(foo); // undefined
var foo = "foo";
console.log(foo); // foo

let aa = 10;
aa++; // 11
console.log(aa);

aa += 100;
console.log(aa); // 111

aa--; // 110
console.log(aa);

// Primitive Data Types in JavaScript

// Number
let num = 42;
console.log("Number:", num, typeof num);

// String
let str = "Hello, World!";
console.log("String:", str, typeof str);

// Boolean
let bool = true;
console.log("Boolean:", bool, typeof bool);

// Undefined
let undef;
console.log("Undefined:", undef, typeof undef);

// Null
let nullValue = null;
console.log("Null:", nullValue, typeof nullValue);

// Symbol
let sym = Symbol("unique");
console.log("Symbol:", sym, typeof sym);

// BigInt
let bigInt = 1234567890123456789012345678901234567890n;
console.log("BigInt:", bigInt, typeof bigInt);

// JavaScript Operators

// 1. Arithmetic Operators
let aaa = 10, bb = 3; // fixed duplicate declaration of b
console.log("Arithmetic:", aaa + bb, aaa - bb, aaa * bb, aaa / bb, aaa % bb, aaa ** bb);
// 10 + 3 = 13
// 10 - 3 = 7
// 10 * 3 = 30
// 10 / 3 = 3.3333333333333335
// 10 % 3 = 1 (remainder)
// 10 ** 3 = 1000 (exponentiation)

// 2. Assignment Operators
let xx = 5;
xx += 2; xx -= 1; xx *= 3; xx /= 2;
console.log("Assignment:", xx); // fixed from `x` to `xx`
// 5 + 2 = 7
// 7 - 1 = 6
// 6 * 3 = 18
// 18 / 2 = 9
// 9 = 9

// 3. Comparison Operators
let cc = 5, d = 10;
console.log("Comparison:", cc == d, cc != d, cc === d, cc !== d, cc > d, cc < d, cc >= d, cc <= d);
// == equal to
// != not equal to
// === equal value and type
// !== not equal value and type
// > greater than
// < less than
// >= greater than or equal to
// <= less than or equal to

// 4. Logical Operators
let e = true, f = false;
console.log("Logical:", e && f, e || f, !e);
// && logical AND
// || logical OR
// ! logical NOT
// true && false = false
// true || false = true

// 5. Unary & Ternary Operators
let g = 5;
console.log("Unary & Ternary:", +g, -g, ++g, --g, g > 0 ? "Positive" : "Negative");
// +g = 5 (unary plus)
// -g = -5 (unary minus)        
// ++g = 6 (increment)
// --g = 5 (decrement)
// g > 0 ? "Positive" : "Negative" = Positive (ternary operator)

// == value comparison(only value is compared)
let zz = 5;

console.log(zz == 5); // true
console.log(zz == 6); // false
console.log(zz == "5"); // true (type coercion)
console.log(zz == "6"); // false (type coercion)

// === value and type comparison (both value and type is compared)
console.log(zz === 5); // true
console.log(zz === 6); // false
console.log(zz === "5"); // false (type coercion), type is string and number
console.log(zz === "6"); // false (type coercion), type is string and number

// != value comparison (only value is compared)
if (zz == 5) {
    console.log("value matched");
}
else if (zz == 6) {
    console.log("value not matched");
}
else {
    console.log("faka!!");
}

//switch case
switch (zz) {
    case 10:
        console.log("value is 10");
        break;
    case 20:
        console.log("value is 20");
        break;
    default:
        console.log("value is not matched");
        break;
}

//loops
//iterate through an array
let arr = [1, 2, 3, 4, 5];

for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}
//output: 1 2 3 4 5

arr.forEach(arr => {
    console.log(arr);
});
//output: 1 2 3 4 5

//while loop
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
//output: 0 1 2 3 4

//do while loop
let j = 0;

do {
    console.log(j);
    j++;
}
while (j < 5)
//output: 0 1 2 3 4

//objects
const person1 = {
    name: "John",
    age: 30,
    city: "New York",
    greet: function () {
        console.log("Hello, my name is " + this.name);
    }
};

person1.greet(); // Hello, my name is John
delete person1.city; // delete city property from person1 object

//Use dot notation (object.property) to get the value.
console.log(person1.name); // John 
console.log(person1["age"]); // 30
console.log(person1.city); // undefined (since deleted)

//array
const fruits = ["apple", "Banana", "cherry"];
console.log(fruits[0]); // apple
console.log(fruits[1]); // Banana

const person = {
    name: "John",
    age: 30,
    city: "New York"
};
delete person.age; // delete age property from person object
console.log(person); // { name: 'John', city: 'New York' }

//for in loop is used to iterate through the properties of an object
for (let key in person) {
    console.log(key + ": " + person[key] + "\n");
}
//output: 
// name: John
// city: New York

//for of loop is used to iterate through the values of an array
const numbers = [1, 2, 3, 4, 5];
for (let number of numbers) {
    console.log(number + "\n");
}
//output: 1 2 3 4 5

//functions
function add(a, b) {
    return a + b;
}
console.log(add(5, 10)); // 15
console.log(add(2, 2)); // 4

function substraction(a, b, c) {
    return (a + b) - c;
}

let ans = substraction(10, 20, 5);
console.log(ans); // 25
