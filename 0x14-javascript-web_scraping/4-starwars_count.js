#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const obj = JSON.parse(body);
  let countChar = 0;
  const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
  for (let i = 0; i < obj.results.length; i++) {
    for (let j = 0; j < obj.results[i].characters.length; j++) {
      if (obj.results[i].characters[j] === charId) {
        countChar++;
      }
    }
  }
  console.log(countChar);
});
