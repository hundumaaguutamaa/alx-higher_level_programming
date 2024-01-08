#!/usr/bin/node
// Reads and prints the content of a file. 

const filesys = require('fs');
const Argmnts = process.argv.slice(2);
filesys.readFile(Argmnts[0], 'utf-8', function (err, data) {
  // Print error
    if (err) {
    console.log(err);
  } 
  else {
    console.log(data);
  }
});
