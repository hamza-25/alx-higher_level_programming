#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else if (argv.length >= 4) {
  const myArray = argv.slice(2).map(value => parseFloat(value)).filter(value => !isNaN(value));
  const nMax = Math.max(...myArray);
  let second = myArray[0];
  for (const num1 in myArray) {
    if (myArray[num1] > second && myArray[num1] !== nMax) {
      second = myArray[num1];
    }
  }
  console.log(second);
}
