const myPromise = new Promise((resolve, reject) => {
  // Simulate an asynchronous task (e.g., fetching data, timeout)
  let success = true; // or false, depending on the condition
  
  if (success) {
    resolve("The operation was successful!");
  } else {
    reject("The operation failed.");
  }
  
});
