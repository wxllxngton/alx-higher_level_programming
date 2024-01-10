### JQuery API

<a href="https://oscarotero.com/jquery/">JQuery Cheat Sheet</a>

Here we learn to use JQuery -> Selectors, AJAX, etc.

Example code:

#### Using selectors

```javascript
$('#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
        $('header').removeClass('green').addClass('red');
    } else {
        $('header').removeClass('red').addClass('green');
    }
});
```

#### Changing CSS

```javascript
$('header').css('color', '#FF0000');
```

#### AJAX Calls

```javascript
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
```

#### Event listeners

```javascript
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
```
