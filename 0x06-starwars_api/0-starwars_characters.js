#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api' + '/films/' + process.argv[2];
  const getBodyJson = (url) => {
    return new Promise((resolve, reject) => {
      request({ url }, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          resolve(JSON.parse(body));
        } else {
          reject(error || new Error(`Status code: ${response.statusCode}`));
        }
      });
    });
  };
  const namesCharacters = async () => {
    try {
      const MoviePromise = await getBodyJson(url);
      const ListApiUrlPromise = MoviePromise.characters.map(getBodyJson);
      const CharactersPromise = await Promise.all(ListApiUrlPromise);
      CharactersPromise.forEach((character) => {
        console.log(character.name);
      });
    } catch (error) {
      console.error(error);
    }
  };
  namesCharacters();
}
