$(document).ready(function() {
  var keyPressed = false;
  var bodyColor = $('body').attr('class');

  $('.large-input').putCursorAtEnd();
  $('.colors .' + bodyColor).addClass('active');

  $(document).keypress(function(evt) {
    if (keyPressed == false) {
      $('.large-input').val('');
      $('.large-input').focus();
      $('#name-helper-text').show();
      keyPressed = true;
    }
    if (evt.keyCode == 32) {
      location.reload(false);
    }
  });

  $('.colors li').on('click', function(evt) {
    var newColor = $(this).attr('class');
    $('.colors .active').removeClass('active');
    $('body').removeClass();
    $('body').addClass(newColor);
    $('#color').val(newColor);
    $(this).addClass('active');
  });
});