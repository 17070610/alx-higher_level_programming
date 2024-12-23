#!/usr/bin/node

const args = process.argv.slice(2);

function add (a, b) {
  return (parseInt(a, 10) + parseInt(b, 10));
}

const a = args[0];
const b = args[1];

console.log(add(a, b));
