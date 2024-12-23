#!/usr/bin/node

const args = process.argv.slice(2);
let i;

if (isNaN(parseInt(args[0], 10))) {
  console.log('Missing size');
} else {
  const size = parseInt(args[0], 10);
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
