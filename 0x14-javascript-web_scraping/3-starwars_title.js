#!/usr/bin/node

const request = require('request');
const MovieId = process.argv[2];
const starWarsUrl = `https://swapi-api.alx-tools.com/api/films/${MovieId}`;

request(starWarsUrl, function (_err, _res, body) {
	body = JSON.parse(body);
	console.log(body.title);
});
