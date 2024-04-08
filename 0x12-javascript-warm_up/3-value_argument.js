#!/usr/bin/node
/* this is printing the first argument */
const fArgs = process.argv[2];
if (fArgs === undefined)
{
	console.log('No argument');
}
else
{
	console.log(fArgs);
}
