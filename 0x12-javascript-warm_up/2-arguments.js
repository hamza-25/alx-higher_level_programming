#!/usr/bin/node
const argv = process.argv;
const argLenght = argv.length;
if (argLenght === 2) {
  console.log('No argument');
} else if (argLenght === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
