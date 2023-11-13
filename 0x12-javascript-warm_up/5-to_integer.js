#!/usr/bin/node
const argv = process.argv;
let i = 0;
for (const element of argv) {
  if (element) {
    i++;
  }
}
const argLenght = i;
if (argLenght === 2) {
  console.log('Not a number');
} else if (argLenght >= 3) {
  if (isNaN(argv[2])) {
	console.log('Not a number');
  } else {
	  console.log('My number: ' + parseInt(argv[2]));
  }
}
