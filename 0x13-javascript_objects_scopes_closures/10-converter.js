#!/usr/bin/node
/* task 10 response */
exports.converter = function (base) {
  function convertToBase (number) {
    if (number < base) {
      return number.toString();
    }
    return convertToBase(Math.floor(number / base)) + (number % base).toString();
  }
  return convertToBase;
};
