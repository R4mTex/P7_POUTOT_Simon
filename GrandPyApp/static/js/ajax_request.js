function script(){
	change_text_send_button()
	send_request()
	show_bloc_historical()
	show_input_historical()
}

function send_request(){
	$.ajax({
		url: '/index_question',
		data: $('form').serialize(),
		type: 'POST',
		success: function(response){
			console.log(response);
		},
		error: function(error){
			console.log(error);
		}
	});
};

function change_text_send_button(){
	if($("#form_send_button").val("Prés à envoyer")) {
		$("#form_send_button").val("Envoyé");
	}
	else {
		$("#form_send_button").val("Prés à envoyer");
	}
};

function show_bloc_historical(){
	if($("#result_question").css("display", "none")) {
		$("#result_question").css("display", "block");
	}
	else {
		$("#result_question").css("display", "none");
	}
};

const input_values = []

function show_input_historical(){
	input_values.push($("#form_input_question").val());
	$("#asked_question").val(input_values);
	console.log(input_values);
};
