
$(document).ready(function(){
    var slideshow_images = $('#slideshow>a');
    slideshow_images.hide();
    var cur_idx = -1;

    function next_image() {
      cur_idx += 1;
      if (cur_idx >= slideshow_images.length) {
        cur_idx = 0;
      }
      $(slideshow_images[cur_idx]).slideDown();
      for (var i; i < slideshow_images.length; i++) {
        if (i != cur_idx) {
          $(slideshow_images[i]).hide();
        }
      }
    }

    $('#slideshow').on('click', function() {
      console.log('woo');
      next_image();
    });
  });
