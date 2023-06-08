#!/usr/bin/node
// searches the second biggest integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.lenght)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
