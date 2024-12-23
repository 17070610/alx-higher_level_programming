#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

const a = args[0];
console.log(factorial(a));
