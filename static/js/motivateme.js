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

  $('.colors li').on('click', function(evt) {
    var newColor = $(this).attr('class');
    $('.colors .active').removeClass('active');
    $('body').removeClass();
    $('body').addClass(newColor);
    $('#color').val(newColor);
    $(this).addClass('active');
  });
});