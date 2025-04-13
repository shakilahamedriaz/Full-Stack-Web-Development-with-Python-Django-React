console.log("Hello, World!");


const  arr = ["a", "b", "shakil" , "is"];

console.log(arr);
//output: [ 'a', 'b', 'shakil', 'is' ]

arr.push("lastindex");

console.log(arr);
//output: [ 'a', 'b', 'shakil', 'is', 'lastindex' ]


//name function
function ghorardim(){
    console.log("ok google!");
} 
ghorardim();
//output: ok google!

//anonymous function
(function(){
    console.log("Anonymous function!");
})

();
//output: Anonymous function!


//Arrow function:
const arrowFunction = () => {
    console.log("Arrow function!");
}

arrowFunction();
//output: Arrow function!




//object:
const person = {
    name: "Shakil",
    age: 22,
    isStudent: true,
    greet: function() {
        console.log("Hello, my name is " + this.name);
    }
}

console.log(person);
//output: { name: 'Shakil', age: 22, isStudent: true, greet: [Function: greet] }

console.log(person.name);
//output: Shakil

console.log(person.age);
//output: 22

console.log(person.function());
//output: Hello, my name is Shakil



