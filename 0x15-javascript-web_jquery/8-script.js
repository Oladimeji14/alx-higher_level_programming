$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    $.getJSON(url, function(data) {
        if (data.results && data.results.length > 0) {
            $.each(data.results, function(index, movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        } else {
            $('#list_movies').append('<li>No movies found</li>');
        }
    }).fail(function() {
        $('#list_movies').append('<li>Error fetching movies</li>');
    });
});
