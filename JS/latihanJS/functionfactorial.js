// program to find the factorial of a number
function factorial(x) {
    let result=1;

    for (let i=1;i<=x;i++) {
        result*=i;
    }
    return result;
}

// take input from the user
const x = 50;

//calling factorial() if num is positive
if (x >= 0){
    const result2 = factorial(x);
    console.log(`The Factorial of ${x} is ${result2}`);
} else {
    console.log("Enter a positive Number.");
}