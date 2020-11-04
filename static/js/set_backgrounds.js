// Create background for the divs representing different colors/patterns

function colors_background() {
    const colors = document.getElementsByClassName("color");
    for (i = 0; i < colors.length; i++) {
        this_el = document.getElementsByClassName("color")[i]
        hex_value = this_el.getAttribute("data-hex");
        this_el.style.backgroundColor = hex_value;
    }

}

function patterns_background() {
    const patterns = document.getElementsByClassName("pattern");
    for (i = 0; i < patterns.length; i++) {
        this_el = document.getElementsByClassName("pattern")[i]
        href_value = this_el.getAttribute("title");
        this_el.style.background = `url(${href_value})`;
    }

}

colors_background()
patterns_background()
