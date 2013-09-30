var currentData;

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
      if (nameEntered === false) {
        $('#name-input').val('');
        $('#name-input').focus();
        $('#name-helper-text').show();
      }
      if (nameEntered === true) {
        $('#task-input').val('');
        $('#task-input').focus();
        $('#task-helper-text').show();
      }
      keyPressed = true;
    }

    if (code === 13) {
      if ($('#questions').length == 0) {
        location.reload();
      }
      if (nameEntered === false) {
        evt.preventDefault();
        nameEntered = true;
        keyPressed = false;
        $('#name-input, #name-helper-text').hide();
        $('#task-input').val('What do you need to do?');
        $('#task-input').show();
        $('#task-input').putCursorAtEnd();
      } else {
        $('#questions').submit();
        var post_name = $('#name-input').val(),
            post_task = $('#task-input').val(),
            post_color = $('#color-input').val(),
            my_data = {'name': post_name, 'task' : post_task, 'color': post_color};

        my_data = JSON.stringify(my_data);
        $.ajax({
          url: '/',
          'type': 'POST',
          data: my_data,
          success: function(data) {
            currentData = $.parseJSON(data);
          }
        });
      }
    }

    if (code === 32) {
      if ($('#questions').length === 0) {
        $.ajax({
          url: '/',
          'type': 'POST',
          data: {'name': 'hi', 'task': 'more'}
        });
      }
    }
  });

  $('.colors li').on('click', function(evt) {
    var newColor = $(this).attr('class');
    $('#favicon').attr('href', 'static/img/' + newColor + '.ico');
    $('.colors .active').removeClass('active');
    $('body').removeClass();
    $('body').addClass(newColor);
    $('#color').val(newColor);
    $(this).addClass('active');
  });
});
