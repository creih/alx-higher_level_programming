#!/usr/bin/node
/* task about chaning datatypes in integer */
const iya1 = parseInt(process.argv[2]);
if (!isNaN(iya1))
{
	console.log(`My number: ${iya1}`);
}
else
{
	console.log('Not a number');
}
