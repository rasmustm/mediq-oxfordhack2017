
(function($) {

	skel.breakpoints({
		xlarge: '(max-width: 1680px)',
		large: '(max-width: 1140px)',
		medium: '(max-width: 980px)',
		small: '(max-width: 736px)',
		xsmall: '(max-width: 480px)',
		xxsmall: '(max-width: 320px)'
	});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 250);
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on mobile.
			skel.on('+mobile -mobile', function() {
				$.prioritize(
					'.important\\28 mobile\\29',
					skel.breakpoint('mobile').active
				);
			});

		// Scrolly.
			$('.scrolly').scrolly();

	});

})(jQuery);

// Start when button is clicked
var buttonClicked = false;
$("#start_button").click(function(){
    //$("#start_button").empty();
		if (buttonClicked == false){
			buttonClicked = !buttonClicked;
			//let startbutton = $("<li><a href='#three' class='button scrolly'>Recording</a></li>");
			//$("#start_button").append(startbutton);
			$("#start_button").addClass('recording');
			$("#searchsubtitle").empty();
			$("#stopBtn").show();
			$("#startBtn").hide();
		}

		// render();
});

title = "Here goes the title"
abstract = "Here goes the abstract."
journalLink = "www.google.nl"

// $().(()){
// 	let article = $("
// 		<div class='row 150%'>
// 			<div class='4u 12u$(medium)'>
// 				<h3>"+title+"</h3>
// 				<p>"+abstract+"</p>
// 				<ul class='actions'>
// 					<li><a href="+journalLink+" class="button">Full article</a></li>
// 				</ul>
// 			</div>"
// 	);
// 	$("#articleposts").append(article);
// });

// Select all links with hashes
/*$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
	  
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '')
      &&
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });*/