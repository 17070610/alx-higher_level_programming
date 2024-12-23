#!/usr/bin/node

const addMeMaybe = function (number, theFunction) {
  const increment = number + 1;
  theFunction(increment);
};

module.exports = { addMeMaybe };
