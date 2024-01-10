const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  // data['results'][0]['title'];
  // console.log(data['results'].length)
  for (let i = 0; i < data.results.length; i++) {
    $('#list_movies').append(data.results[i].title);
  }
  // $('#list_movies').text(data['results'][0]['title']);
}, 'json');
