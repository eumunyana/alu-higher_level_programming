#!/usr/bin/node
// Prints the first arguments to it

if (process.argv[2] === undefined) {
	console.log('No argument');	
} else {
	console.log(process.argv[2]);
}
