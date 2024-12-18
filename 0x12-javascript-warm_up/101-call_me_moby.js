#!/usr/bin/node

let i;
const callMeMoby = function (x, theFunction) {
  for (i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports = { callMeMoby };
