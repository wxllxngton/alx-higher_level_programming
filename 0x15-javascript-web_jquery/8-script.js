'use-strict';

/**
 * Script that fetches and lists the title for all movies
 * by using this URL:
 * https://swapi-api.alx-tools.com/api/films/?format=json
 */

const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.ajax({
    type: 'GET',
    url: URL,
    success: function (data) {
        // Iterate over each movie in the data array
        const movies = data.results;
        $.each(movies, (index, movie) => {
            $('#list_movies').append(`<li>${movie.title}</li>`);
        });
    },
});
