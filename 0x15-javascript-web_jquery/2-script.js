'use-script';

/**
 * Script that updates the text color of the <header>
 * element to red (#FF0000) when the user clicks on the
 * tag DIV#red_header
 */

const header = document.querySelector('header');
const divRedHeader = document.querySelector('#red_header');

divRedHeader.addEventListener('click', () => {
    // Change the style property "color" of the header element
    header.style.color = '#ff0000';
});
