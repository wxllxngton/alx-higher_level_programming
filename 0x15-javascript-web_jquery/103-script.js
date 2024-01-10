'use strict';

/**
 * Script fetches and prints how to say “Hello”
 * depending on the language.
 * Also works with ENTER.
 */

const URL = 'https://hellosalut.stefanbohacek.dev/';

const fetchPrint = function () {
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
};

$(function () {
    $('#btn_translate').click(fetchPrint);
    $('#language_code').keypress((e) => {
        const key = e.which;
        if (key === 13)
            // Enter was pressed
            fetchPrint();
        else return;
    });
});
