(function($) {

	"use strict";

	function hideSubmitButton(form_id) {
		$("#"+form_id).find("[type='submit']").hide();
		
	}

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$(".toggle-password").click(function() {

	  $(this).toggleClass("fa-eye fa-eye-slash");
	  var input = $($(this).attr("toggle"));
	  if (input.attr("type") == "password") {
	    input.attr("type", "text");
	  } else {
	    input.attr("type", "password");
	  }
	});

	function validateForm(form_id) {
		if (!$("#"+form_id).valid()){
			return false;
		}
		hideSubmitButton($("#"+form_id).attr("id"));
		return true;
	}

	$("#login-form").on("submit", function(e){
		return validateForm($(this).attr("id"))
	})
	
	$("#reset-password-form").on("submit", function(e){
		return validateForm($(this).attr("id"))
	})
	
	$("#reset-pass-form").on("submit", function(e){
		return validateForm($(this).attr("id"))
	})



})(jQuery);