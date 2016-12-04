$(document).ready(function(){ "use strict";
    $("#navbar ul li").hover(function() { 
		$(this).find("ul").stop().slideToggle(400);		
	});	
});
