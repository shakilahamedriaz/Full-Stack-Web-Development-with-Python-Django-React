//printing hello world in js
console.log("Hello World");
console.log("hello duniya!!");

//variable declaration 
let x = 5;
console.log("hey there!! {x}");

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
var b = 30; // redeclaring var is allowed


console.log(a); // 10
console.log(b); // 30



var c;
console.log(c); // undefined
c = 10;
console.log(c); // 10


//var:
console.log(foo);// undefined
var foo = "foo";
console.log(foo); // foo

let aa = 10;
aa++; // 11
console.log(aa);

aa +=100;
console.log(aa); // 111

aa--; // 110
console.log(aa);


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
else{
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

for(let i = 0; i < arr.length; i++)
{
    console.log(arr[i]);
}
//output: 1 2 3 4 5

arr.forEach(arr => {
    console.log(arr);
});
//output: 1 2 3 4 5


//while loop
let i = 0;
while(i < 5)
{
    console.log(i);
    i++;
}

//output: 0 1 2 3 4


//do while loop
let j = 0;

do
{
    console.log(j);
    j++;
}
while(j < 5)
//output: 0 1 2 3 4


//objects
const person = {
    name: "John",
    age: 30,
    city: "New York"
};
//Use dot notation (object.property) to get the value.
console.log(person.name); // John 
console.log(person["age"]); // 30


//for in loop is used to iterate through the properties of an object
for(let key in person)
{
    console.log(key + ": " + person[key] + "\n");
}
//output: 
// name: John
//age: 30
//city: New York



//functions
function add(a, b) {
    return a + b;
}
console.log(add(5, 10)); // 15


function substraction(a, b, c){
    return (a + b ) - c;
}

let ans = substraction(10, 20, 5);
console.log(ans); // 25 