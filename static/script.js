$(document).ready(function() {
    $(".spin").hide();
   
    $('input[type=submit]').on("click", function() {
        $('.spin').show();
    });
});