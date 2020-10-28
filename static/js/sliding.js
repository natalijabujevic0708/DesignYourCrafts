$(document).ready(function () {
    $("#colors_title").click(function () {
        $(".colors").slideToggle("slow");
    });
    $("#patterns_title").click(function () {
        $(".patterns").slideToggle("slow");
    });
    $("#text_title").click(function () {
        $("#text_options").slideToggle("slow");
        $("#text_area_div").toggle();
    });
    $("#decorations_title").click(function () {
        $("#decoration_options").slideToggle("slow");
    });
});
