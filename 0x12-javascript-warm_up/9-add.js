#!/usr/bin/node

const args = process.argv.slice(2);

function add(a, b) {
  return (parseInt(a, 10) + parseInt(b, 10));
}

let a = args[0];
let b = args[1];

console.log(add(a, b));
