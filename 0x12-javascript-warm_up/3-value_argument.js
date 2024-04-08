#!/usr/bin/node
/* this is printing the first argument */
let fArgs = process.argv.length - 1;
if (fArgs === 0)
{
	console.log('No argument');
}
else
{
	console.log(fArgs);
}
