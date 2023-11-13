#!/usr/bin/node
function factiral (n) {
  if (n === 1) {
    return 1;
  }
  return n * factiral(n - 1);
}
const argv = process.argv;
if (argv.length === 2) {
  console.log(1);
} else if (argv.length >= 3) {
  const fNum = parseInt(argv[2]);
  if (typeof (fNum) === 'number') {
    console.log(factiral(fNum));
  }
}
