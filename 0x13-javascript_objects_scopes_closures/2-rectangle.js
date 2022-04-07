#!/usr/bin/node
class Rectangle {
  constructor(width, height) {
    if (width > 0 && height > 0 && width !== undefined && height !== undefined) {
      this.width = width;
      this.height = height;
    }
  }
}
module.exports = Rectangle;
