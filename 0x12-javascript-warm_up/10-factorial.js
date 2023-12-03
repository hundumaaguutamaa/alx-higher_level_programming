#!/usr/bin/node
const i = process.argv[2];

function factorial (i) {
  if (i === 0 || i === 1 || i === undefined || isNaN(i)) {
    return 1;
  } else { return (i * factorial(i - 1));
}
console.log(factorial(Number(i)));
