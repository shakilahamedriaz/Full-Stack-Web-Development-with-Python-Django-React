function validation(){
    const inputObj = document.getElementById('id1');

    if(inputObj.validity.rangeOverflow){

        inputObj.setCustomValidity("You have mad a range Overflow!");

    }else if(inputObj.validity.rangeUnderflow){

        inputObj.setCustomValidity("You have made a range Underflow");
    }else if(inputObj.validity.valueMissing){
        
        inputObj.setCustomValidity("Value Missing!");
    }


    if(!inputObj.checkValidity()){

        document.getElementById("demo").innerHTML =  inputObj.
        validationMessage;

    }
}