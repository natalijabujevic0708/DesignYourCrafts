$("#box_top").click(function () {
    $('.full_box').css("display", "none")
    $('.top_box').css("display", "inline").addClass("active_svg")
    $('#box_full').removeClass("border")
    $(this).addClass("border")
    $('.bottom_box').removeClass("active_svg")
});
$("#box_bottom").click(function () {
    $('.full_box').css("display", "none")
    $('.bottom_box').css("display", "inline").addClass("active_svg")
    $('#box_full').removeClass("border")
    $(this).addClass("border")
    $('.top_box').removeClass("active_svg")
});
$("#box_full").click(function () {
    $('.top_box, .bottom_box').css("display", "none").removeClass("active_svg")
    $('#box_top, #box_bottom').removeClass("border")
    $(this).addClass("border")
    $('.full_box').css("display", "inline")                                                       
    
});