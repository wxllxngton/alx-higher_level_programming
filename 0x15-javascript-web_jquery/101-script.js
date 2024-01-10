'use-strict';

/**
 * Script that adds, removes and clears
 * LI elements from a list when the user clicks:
 */

$(function () {
    // Add item
    $('#add_item').click(() => {
        $('.my_list').append('<li>Item</li>');
    });

    // Remove item
    $('#remove_item').click(() => {
        $('.my_list li:last-child').remove();
    });

    // Clears list
    $('#clear_list').click(() => {
        $('.my_list').empty();
    });
});
