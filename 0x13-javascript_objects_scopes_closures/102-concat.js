#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
fs.readFile(args[2], 'utf8', (err, data1) => {
  if (err) {
    return;
  }
  fs.appendFile(args[4], data1, 'utf8', (err) => {
    if (err) {
      console.error('Error append file:', err);
    }
  });
});
fs.readFile(args[3], 'utf8', (err, data2) => {
  if (err) {
    return;
  }
  fs.appendFile(args[4], data2, 'utf8', (err) => {
    if (err) {
      console.error('Error append file:', err);
    }
  });
});
