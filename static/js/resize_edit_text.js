//Draggable functionality
$(function () {
    $('#text_area_div').draggable()
});

//Change font-size
$('#font_slide').on('input', function () {
    slide_value = parseInt($('#font_slide').val())
    $('#textarea').css("font-size", slide_value);
});

//Change font-family
$('#font_family').on('input', function () {
    font_family_value = $('#font_family').val()
    $('#textarea').css("font-family", font_family_value);
});





