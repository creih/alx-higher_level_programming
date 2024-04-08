#!/usr/bin/node
/* this is about if else nd else if. */
const nArgs = process.argv.length - 2;
if (nArgs === 0)
{
  console.log('No argument');
}
else if (nArgs === 1)
{
  console.log('Argument found');
}
else
{
  console.log('Arguments found');
}
