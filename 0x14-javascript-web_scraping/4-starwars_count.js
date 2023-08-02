#!/usr/bin/node

const request = require('request');
const starWarsUrl = process.argv[2];
let times = 0;

request(starWarsUrl, function (error, response, body) {
	body = JSON.parse(body).results;

	for (let i = 0; i < body.length; ++i) {
		const characters = body[i].characters;

		for (let j = 0; j < characters.length; ++j) {
			const character = characters[j];
			const characterId = character.split('/')[5];

			if (characterId === '18') {
				times += 1;
			}
		}
	}

	console.log(times);
});