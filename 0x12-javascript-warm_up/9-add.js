#!/usr/bin/node
function add(a, b) {
	return (a + b);
}
const argv = process.argv;
if (argv.length === 2) {
  console.log('NaN');
} else if (argv.length >= 3) {
  const fNum = parseInt(argv[2]);
  const sNum = parseInt(argv[3]);
  if (typeof (fNum) === 'number' && typeof (sNum) === 'number') {
    console.log(add(fNum, sNum));
  }
} else {
  console.log('NaN');
}
