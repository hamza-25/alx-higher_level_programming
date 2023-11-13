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
  console.log(argv[2] + ' is ' + argv[3]);
} else if (argLenght >= 3) {
  console.log(argv[2] + ' is ' + argv[3]);
}
