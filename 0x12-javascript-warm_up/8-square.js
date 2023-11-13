#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log('Missing size');
} else if (argv.length >= 3) {
  const num = parseInt(argv[2]);
  if (typeof (num) === 'number' && num > 0) {
    for (let i = 0; i < num; i++) {
      let j = 0;
      let str = '';
      for (; j < num; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}
