$(document).ready(function() {
  var keyPressed = false,
      nameEntered = false,
      bodyColor = $('body').attr('class');

  // Puts cursor at end of input
  $('#name-input').putCursorAtEnd();

  // Changes background color
  $('.colors .' + bodyColor).addClass('active');

  $(document).keypress(function(evt) {
    var code = (evt.keyCode ? evt.keyCode : evt.which);

    if (keyPressed == false) {
      if (nameEntered == false) {
        $('#name-input').val('');
        $('#name-input').focus();
        $('#name-helper-text').show();
      }
      if (nameEntered == true) {
        $('#task-input').val('');
        $('#task-input').focus();
        $('#task-helper-text').show();
      }
      keyPressed = true;
    }

    if ((code == 13) && (nameEntered == false)) {
      evt.preventDefault();
      nameEntered = true;
      keyPressed = false;
      $('#name-input, #name-helper-text').hide();
      $('#task-input').val('What do you need to do?');
      $('#task-input').show();
      $('#task-input').putCursorAtEnd();
    } else if (evt.keyCode == 13) {
      $('form').submit();
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