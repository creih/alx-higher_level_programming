#!/usr/bin/node
const bare = parseInt(process.argv.slice(2).map(Number));

bare.sort((a, b) => b- a);
if (bare.length === 0 || bare.length === 1) {
  console.log(0);
}  else {
  console.log(bare[1]);
}
