// Apply the color or pattern to the svg element

const overlay = document.getElementsByClassName("active_svg");

function changeColor() {
  // get the hex color
  var color = document.getElementById("color_picker").value

  // Set the fill style
  for (var i = 0; i < overlay.length; i++) {
    overlay[i].style.fill = color;
  }
}
// Click on a pattern
var el = document.getElementsByClassName("pattern");
for (var i = 0; i < el.length; i++) {
  el[i].onclick = changePattern;
}

function changePattern(e) {
  // get the url
  let url_pattern = e.target.getAttribute("id");

  // set the url
  for (var i = 0; i < overlay.length; i++) {
    overlay[i].style.fill = `url(#${url_pattern})`;
  }
}

// Click on a decoration
var el = document.getElementsByClassName("decoration");
for (var i = 0; i < el.length; i++) {
  el[i].onclick = applyDecoration;
}

function applyDecoration(e) {
  // get the url
  let src_decoration = e.target.getAttribute("title");
  // display decoration
  document.getElementsByClassName("chosen_decoration")[0].src = src_decoration;
  document.getElementById("chosen_decoration_div").style.display = "block";
}


