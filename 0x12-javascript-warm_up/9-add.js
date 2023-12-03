#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('Invalid input. Please provide two integers.');
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
