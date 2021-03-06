// Create tabs for design options
function openEditOption(evt, editOption) {
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  if (editOption == 'Pattern') {
    document.getElementById(editOption).style.display = "flex";
  } else {
    document.getElementById(editOption).style.display = "block";
  }

  evt.currentTarget.className += " active";

}
