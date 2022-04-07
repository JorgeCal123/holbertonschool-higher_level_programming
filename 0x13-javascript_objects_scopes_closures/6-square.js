#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let ms = 'X';
    if (c !== undefined) {
      ms = c;
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s = s + ms;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
