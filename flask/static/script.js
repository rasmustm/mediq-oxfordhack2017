function startDictation() {

    if (window.hasOwnProperty('webkitSpeechRecognition')) {

      var recognition = new webkitSpeechRecognition();

      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.lang = "en-US";
      recognition.start();

      recognition.onresult = function(e) {
        document.getElementById('transcript').value
                                 = e.results[0][0].transcript;
      recognition.stop();
      document.getElementById('test').submit();
      };

      recognition.onerror = function(e) {
        recognition.stop();
      }

    }
  }

$(document).ready(function() {
	$("#microphoneButton").click(function () {
		$(this).toggleClass("red");
	});
});
