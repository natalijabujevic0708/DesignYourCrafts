// Sliding animation of the divs 
$(document).ready(function () {
    $("#colors_title").click(function () {
        $(".colors").slideToggle("slow").css("display", "flex");
    });
    $("#patterns_title").click(function () {
        $(".patterns").slideToggle("slow").css("display", "flex");
    });
    $("#text_title").click(function () {
        $("#text_options").slideToggle("slow");
        $("#text_area_div").show()
    });
    $("#decorations_title").click(function () {
        $("#decoration_options").slideToggle("slow");
    });
});
