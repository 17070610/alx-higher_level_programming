#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(parseInt(args[0], 10)) || parseInt(args[0], 10) <= 0) {
  console.log('Missing number of occurences')
} else {
  for (i = 0; i < parseInt(args[0], 10); i++) {
	  console.log('C is fun')
  }
}
