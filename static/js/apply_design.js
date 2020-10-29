// Apply the color or pattern to the svg element

const overlay = document.getElementById("product-shape");

// Click on a color
var el = document.getElementsByClassName("color", "pattern");
for (var i = 0; i < el.length; i++) {
  el[i].onclick = changeColor;
}

function changeColor(e) {
  // get the hex color
  let hex = e.target.getAttribute("data-hex");
  // set the hex color
  overlay.style.fill = hex;
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
  overlay.style.fill = `url(#${url_pattern})`;
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


