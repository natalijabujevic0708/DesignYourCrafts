// Apply the color or pattern to the svg element
const overlay = document.getElementsByClassName("active_svg");

// Apply color
function changeColor() {
  // Get the hex color
  var color = document.getElementById("color_picker").value

  // Set the fill style
  for (var i = 0; i < overlay.length; i++) {
    overlay[i].style.fill = color;
  }
}

// Apply pattern
var pattern_elements = document.getElementsByClassName("pattern");
// Add onclick event listener for all the pattern divs
for (var i = 0; i < pattern_elements.length; i++) {
  pattern_elements[i].onclick = changePattern;
}

function changePattern(element) {
  // Get the url
  let url_pattern = element.target.getAttribute("id");

  // Set the fill style
  for (var i = 0; i < overlay.length; i++) {
    overlay[i].style.fill = `url(#${url_pattern})`;
  }
}

// Apply decoration
var decoration_elements = document.getElementsByClassName("decoration");
// Add onclick event listener for all the decoration divs
for (var i = 0; i < decoration_elements.length; i++) {
  decoration_elements[i].onclick = applyDecoration;
}

// Function to delete ids representing active decorations
function deleteActiveId(elements) {
  if (elements) {
    elements.removeAttribute("id")
  }
}
function deleteAllId() {
  active_decorations = document.getElementById("active_decoration")
  deleteActiveId(active_decorations)
  close_decoration = document.getElementById("close_decoration")
  deleteActiveId(close_decoration)
  active_decoration_div = document.getElementById("active_decoration_div")
  deleteActiveId(active_decoration_div)
}

// Function to display a decoration
function applyDecoration(el) {
  let src_decoration = el.target.getAttribute("src");
  let id_decoration = el.target.getAttribute("id");
  deleteAllId()

  // Create a clone of the div element, add span and image elements as children
  let clone = document.querySelector('#original_decoration_div').cloneNode(true)
  var close = document.createElement("span")
  close.id = "close_decoration"
  close.innerHTML = "X"
  clone.appendChild(close)
  var img = document.createElement("img");
  img.src = src_decoration;
  img.className = "decoration_image"
  img.id = "active_decoration"
  clone.appendChild(img)
  clone.setAttribute("id", "active_decoration_div")
  document.getElementById("decoration_container").appendChild(clone);

  $('.chosen_decoration_div').draggable()

  // Click on a visible decoration
  var image_decoration = document.getElementsByClassName("decoration_image");

  for (var i = 0; i < image_decoration.length; i++) {
    image_decoration[i].onclick = activeDecoration;
  }
  // Function to make the decoration active after a user clicks on it
  function activeDecoration(e) {
    deleteAllId()
    e.target.previousElementSibling.setAttribute("id", "close_decoration")
    e.target.parentNode.setAttribute("id", "active_decoration_div")
    e.target.setAttribute("id", "active_decoration")
  }

  // Close functionality
  var makeVisible = function () {
    $('#close_decoration').css("visibility", "visible")
  }
  $('#active_decoration_div').click(makeVisible).mouseenter(makeVisible);
  $("#active_decoration_div").mouseleave(function () {
    $('#close_decoration').css("visibility", "hidden")
  });
  $("#close_decoration").click(function () {
    $('#active_decoration_div').remove()
  });
}





