#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode)
});