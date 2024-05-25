#!/usr/bin/node
const request = require('request');
if (process.argv.length === 3) {
  const url = 'https://swapi-api.alx-tools.com/api' + '/films/' + process.argv[2];
  request({ url }, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      JSON.parse(body).characters.forEach((api) => {
        request(api, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            console.log(JSON.parse(body).name);
          }
        });
      }
      );
    }
  });
}
