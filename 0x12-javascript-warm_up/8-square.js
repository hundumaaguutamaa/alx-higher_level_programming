#!/usr/bin/node

const size = parseInt(process.argv[2]) || 1;

if (isNaN(size)) {
  console.log('Invalid size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
