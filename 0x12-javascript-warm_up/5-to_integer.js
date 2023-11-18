#!/usr/bin/node

const process = require('process');

const firstArg = process.argv[2];
const convertFirstArg = parseInt(firstArg);

if (!isNaN(convertFirstArg)) {
  console.log('My number:', convertFirstArg);
  
}
else {
  console.log('Not a number');
}
