'use strict';

/**
 * Script that toggles the class of the <header> element
 * when the user clicks on the tag DIV#toggle_header
 */

$('#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
        $('header').removeClass('green').addClass('red');
    } else {
        $('header').removeClass('red').addClass('green');
    }
});
