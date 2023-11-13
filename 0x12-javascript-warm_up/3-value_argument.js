#!/usr/bin/node
const argv = process.argv;
let i = 0;
for (const element of argv) {
  i++;
}
const argLenght = i;
if (argLenght === 2) {
  console.log('No argument');
} else if (argLenght >= 3) {
  console.log(argv[2]);
}/* else {
  console.log('Arguments found');
} */
