import * as readlineSync from "readline-sync";

function calculator(): void {
  console.log("Simple Calculator");
  const num1 = parseFloat(readlineSync.question("Enter the first number: "));
  const operator = readlineSync.question("Enter an operator (+, -, *, /): ");
  const num2 = parseFloat(readlineSync.question("Enter the second number: "));

  let result: number;

  if (operator === "+") {
    result = num1 + num2;
  } else if (operator === "-") {
    result = num1 - num2;
  } else if (operator === "*") {
    result = num1 * num2;
  } else if (operator === "/") {
    if (num2 === 0) {
      console.log("Cannot divide by zero.");
      return;
    }
    result = num1 / num2;
  } else {
    console.log("Invalid operator.");
    return;
  }

  console.log(`Result: ${result}`);
}

calculator();
