#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(parseInt(args[0], 10))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[0], 10));
}
