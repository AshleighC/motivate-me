$(document).ready(function() {
  var keyPressed = false;
  $('#name-input').putCursorAtEnd();

  $(document).keypress(function() {
    if (keyPressed == false) {
      $('#name-input').val('');
      $('#name-input').focus();
      keyPressed = true;
    }
  });
});
