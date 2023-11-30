if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}
$(document).ready(function() {
    click_btn();
    $('body').on('keyup', function(event) {
        if (event.keyCode == 13) {
            $('#btn').click();
        }
    });
});
