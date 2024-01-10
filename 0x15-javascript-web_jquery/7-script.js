'use-strict';

/**
 * Script that fetches the character name from this URL:
 * https://swapi-api.alx-tools.com/api/people/5/?format=json
 */

const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

/* Shorthand for $(document).ready(function() {} */
$(function () {
    $.ajax({
        type: 'GET',
        url: URL,
        success: function (characterData) {
            $('#character').text(characterData.name);
        },
    });
});
