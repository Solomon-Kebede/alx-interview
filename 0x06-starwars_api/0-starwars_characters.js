#!/usr/bin/node
const request = require('request');
const args = process.argv;

if (args.length > 2) {
  const filmId = args[2];
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  const charactersObject = {};
  const characters = [];
  request(filmUrl, (error, response, body) => {
    if (error) { return error; }
    const chars = JSON.parse(body).characters;
    for (const c of chars) {
      characters.push(c);
      request(c, (e, r, body) => {
        const name = `${JSON.parse(body).name}`;
        charactersObject[c] = name;
      });
    }
  });
  setTimeout(() => {
    characters.forEach((key) => {
      console.log(charactersObject[key]);
    });
  }, 5000);
}
