#!/usr/bin/node
// Prints the first arguments to it

if (process.argv[2] === undefinied) {
	console.log('No  argument');	
} else {
	console.log(process.argv[2]);
}
