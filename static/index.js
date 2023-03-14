function click_btn() {
    $('body').on('click', '#btn', function() {
        var a = $('#inp').val();
        $.post('/', {'text': a})
        .done(function(data) {
            $('body').html(data);
            click_btn();
        });
    });
}
$(document).ready(function() {
    click_btn();
    $('body').on('keyup', function(event) {
        if (event.keyCode == 13) {
            $('#btn').click();
        }
    });
});
