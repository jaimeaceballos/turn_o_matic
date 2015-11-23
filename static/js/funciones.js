$(document).ready(function() {
	$("#id_documento").addClass("form-control");
	$("#id_documento").attr("required","required");
	$("#id_derivado_a").addClass("form-control");
	$("#id_derivado_a").attr("required","required");
	$("#id_tramite").change(function(){
		$("#tramite").fadeOut();
		setTimeout(
		  function() 
		  {
			$("#documento").fadeIn();
		  }, 400);
	});
});



