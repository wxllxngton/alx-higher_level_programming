'use strict';

/**
 * Script fetches and prints how to say “Hello”
 * depending on the language
 */

const URL = 'https://hellosalut.stefanbohacek.dev/';

$(function () {
    $('#btn_translate').click(() => {
        const langCode = $('#language_code').val();

        if (!langCode) return;

        $.ajax({
            type: 'POST',
            data: {
                lang: langCode,
            },
            url: URL,
            success: function (data) {
                const translation = data.hello;
                $('#hello').text(translation);
            },
        });
    });
});
