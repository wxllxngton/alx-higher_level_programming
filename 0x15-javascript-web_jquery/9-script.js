'use-strict';

/**
 * Script that fetches from
 * https://hellosalut.stefanbohacek.dev/?lang=fr
 * and displays the value of hello from that fetch
 * in the HTML tag DIV#hello.
 */

const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(function () {
    // Fetch data from server
    $.ajax({
        type: 'GET',
        url: URL,
        success: function (data) {
            const translation = data.hello;
            $('#hello').text(translation);
        },
    });
});
