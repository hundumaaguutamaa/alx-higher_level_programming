#!/usr/bin/node

const i = process.argv[2];

function factorial(i) {
  // Base cases: 0! and 1! are both 1
  if (i === 0 || i === 1 || i === undefined || isNaN(i)) {
    return 1;
  } else {
    // Recursive case: i! = i * (i-1)!
    return i * factorial(i - 1);
  }
}

console.log(factorial(Number(i)));
