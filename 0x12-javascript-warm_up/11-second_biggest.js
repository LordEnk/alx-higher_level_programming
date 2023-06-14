#!/usr/bin/node

if (process.argv.length <= 2) {
	console.log(0);
} else if (process.argv.length === 3) {
	console.log(0);
} else {
	let largest = Number.MIN_SAFE_INTEGER;
	let secondl = Number.MIN_SAFE_INTEGER;

	for (let i = 2; i < process.argv.length; i++) {
		const current = parseInt(process.argv[i]);

		if (current > largest) {
			secondl = largest;
			largest = current;
		} else if (current > secondl && current < largest) {
			secondl = current;
		}
	}

	if (seondl === Number.MIM_SAFE_INTEGER) {
		console.log(0);
	} else {
		console.log(${secondl});
	}
}
