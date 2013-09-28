$(document).ready(function() {
  var keyPressed = false;
  $('#name-input').putCursorAtEnd();

  $(document).keypress(function(evt) {
    if (keyPressed == false) {
      $('#name-input').val('');
      $('#name-input').focus();
      $('#name-helper-text').show();
      keyPressed = true;
    }
  });
});
