#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  if (typeof number !== 'number' || !Number.isInteger(number)) {
    return;
  }
  number = number + 1;
  theFunction(number);
};
