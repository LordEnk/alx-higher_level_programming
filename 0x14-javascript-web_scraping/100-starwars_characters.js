t request = require('request');
const movieId = process.argv[2];
const starWarsUrl = https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(starWarsUrl, function (_err, _res, body) {
	const characters = JSON.parse(body).characters;

	for (let i = 0; i < characters.length; ++i) {
		request(characters[i], function (_cErr, _cRes, cBody) {
			console.log(JSON.parse(cBody).name);
		});
	}
});
