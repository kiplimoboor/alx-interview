#!/usr/bin/node

/* eslint-disable space-before-function-paren */

const request = require('request');
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
const peopleUrl = 'https://swapi-api.alx-tools.com/api/people/';

fetchData(peopleUrl, (people) => {
  const filmChars = people.filter((person) => person.films.includes(filmUrl));
  for (const character of filmChars) {
    console.log(character.name);
  }
});

function fetchData(url, callback, results = []) {
  request(url, (err, res, body) => {
    if (err) throw new Error(err);
    if (res.statusCode !== 200) throw new Error('Non 200 status code');
    const data = JSON.parse(body);
    results.push(...data.results);
    if (data.next) {
      fetchData(data.next, callback, results);
    } else {
      callback(results);
    }
  });
}
