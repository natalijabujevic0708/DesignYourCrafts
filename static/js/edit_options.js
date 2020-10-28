//Draggable functionality
$(function () {
    $('#text_area_div, .decorations').draggable()
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

//Resize decoration
$('#image_size_slide').on('input', function () {
    slide_value = parseInt($('#image_size_slide').val())
    $('.decoration').css("height", slide_value);
    $('.decoration').css("width", slide_value);
});

// Decorations edit

var transformX,transformY, transformZ, transformSkew
transformY = 'rotateY(0deg)'
transformX = 'rotateX(0deg)'
transformZ = 'rotateZ(0deg)'
transformSkew = 'skew(0deg)'

//Skew decoration
$('#image_skew_slide').on('input', function () {
    slide_value = parseInt($('#image_skew_slide').val())
    transformSkew ='skew(' + slide_value + 'deg)';
    $('.decoration').css('transform',`${transformY} ${transformZ} ${transformSkew} ${transformX}`);
    return transformSkew
});

//Rotate decoration X-axis
$('#image_rotateX_slide').on('input', function () {
    slide_value = parseInt($('#image_rotateX_slide').val())
    transformX ='rotateX(' + slide_value + 'deg)';
    $('.decoration').css('transform',`${transformY} ${transformZ} ${transformSkew} ${transformX}`);
    return transformX
});

//Rotate decoration Y-axis
$('#image_rotateY_slide').on('input', function () {
    slide_value = parseInt($('#image_rotateY_slide').val())
    transformY ='rotateY(' + slide_value + 'deg)';
    $('.decoration').css('transform',`${transformY} ${transformZ} ${transformSkew} ${transformX}`);
    return transformY
    
});

//Rotate decoration Z-axis
$('#image_rotateZ_slide').on('input', function () {
    slide_value = parseInt($('#image_rotateZ_slide').val())
    transformZ ='rotateZ(' + slide_value + 'deg)';
    $('.decoration').css('transform',`${transformY} ${transformZ} ${transformSkew} ${transformX}`);
    return transformZ
});
