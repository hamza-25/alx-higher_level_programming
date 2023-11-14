#!/usr/bin/node
const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let format = '';
      for (let j = 0; j < this.width; j++) {
        if (typeof (c) === 'undefined') {
          format += 'X';
        } else {
          format += c;
        }
      }
      console.log(format);
    }
  }
}
module.exports = Square;
