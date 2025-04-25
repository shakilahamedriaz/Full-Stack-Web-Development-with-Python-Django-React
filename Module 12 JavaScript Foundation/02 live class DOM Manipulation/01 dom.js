// Select all <h1> tags and log the first one
const first = document.getElementsByTagName("h1");
console.log(first[0]);  // Logs: <h1>Hello bro!</h1>


// Select the paragraph with id="ok"
const kidnapped = document.getElementById("ok");
console.log(kidnapped);  // Logs the selected <p> element


// Change the innerHTML of the paragraph (overwrites all inner content including tags if any)
kidnapped.innerHTML = "I am kidnapped by Shakil!";


// Select the paragraph with id="lala"
const second = document.getElementById("lala");
console.log(second);  // Logs the <p> with id="lala"


// Change the visible text content using innerText (ignores HTML formatting inside)
second.innerText = "hey you kidnapper naki, im from js file!";


// Again select all <h1> elements and modify the second one (index 1)
const temp = document.getElementsByTagName("h1");
temp[1].textContent = "hey- ja ase tai tule daw";  // Change the text content of the second <h1>
console.log(temp[1]);  // Logs modified <h1>


// Define a function to change background color of the paragraph with id="okk"
function changeBG() {  
    const bg = document.getElementById("okk"); // Target the <p> with id="okk"
    bg.style.backgroundColor = "red";  // Change its background to red
}


// Select the button with id="button-id"
const change = document.getElementById("button-id");


// Add a click event listener to the button that will execute changeBG() when clicked
change.addEventListener("click", changeBG);
change.addEventListener("mouseover", changeBG);  // This line is redundant; the function is already added above
//change.addEventListener("mouseout", changeBG);  // This line is also redundant; the function is already added above