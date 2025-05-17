// Function to get GitHub user data by username
function getGithubUserName(username) {

   // Return a Promise because fetch is asynchronous
   return new Promise((resolve, reject) => {
     
     // Call GitHub API with the given username
     fetch(`https://api.github.com/users/${ username }`)

        // If fetch is successful
        .then((Response) => {
            // Convert response to JSON and resolve the promise
            return resolve(Response.json());
        })

        // If an error occurs during fetch
        .catch((error) => 
            // Reject the promise with an error message
            reject(`Network error: ${error.message}`)
        );
        
    });

}

//Call the function and get the user data
getGithubUserName("shakilahamedriaz").then((user) => {
      // Print user data to console
      console.log("Github User Data: ", user);
});
