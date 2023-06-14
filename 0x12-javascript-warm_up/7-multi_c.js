#!/usr/bin/node

let X = parseInt(process.argv[2]);
if (isNaN(X) || process.argv[2]) {
	 while (X > 0) {
		 console.log('C is fun');
		 X--;
	 } else {
		 console.log('Missing number of occurences');
}
