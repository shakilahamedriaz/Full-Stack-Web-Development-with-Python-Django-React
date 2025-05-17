// Create a Promise
const promise = new Promise((resolve, reject) => {

    let success = true; // change to true/false to test 'resolve'/'reject'
    if (success) {
        resolve("Everything was fine bro!");
    } else {
        reject("Something was wrong!");
    }
    
});

// Handle the result of the Promise
promise
    .then((result) => {
        console.log("inside then:");
        console.log(result);  // Output when resolved
    })
    .catch((error) => {
        console.log("inside catch:");
        console.log(error);   // Output when rejected
    })
    .finally(() => {
        console.log("Finally run: ");

    });


/*
        Inside Promise: you only decide what happens (resolve/reject).
        Outside with .then()/.catch(): you react to the result (show message, do something).
 */    
