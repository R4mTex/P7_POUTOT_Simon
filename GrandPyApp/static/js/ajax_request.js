function script(){
	if($("#form_input_question").val() != ""){
		change_text_form()
		send_request()
		test_rotation()
		show_history_bloc()
		show_history_input()
	}
	else{
	}
}

$(document).on('keypress', function(event) {
    if(event.which == 13) {
        script()
    }
});

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

function change_text_form(){
	const btn = $("#form_send_button")
	const input = $("#form_input_question")
	if(btn.val("Prés à envoyer")){
		btn.val("Envoyé");
	}
	else{
		btn.val("Prés à envoyer");
	}
	setTimeout(() => {
		btn.val("Prés à envoyer")
		input.val("")
	}, 3000);
};

function show_history_bloc(){
    const res = $("#result_question")
	if(res.css("display", "none")){
		res.css("display", "block");
	}
	else{
		res.css("display", "none");
	}
};

const input_values = []
i = -1

function show_history_input(){
	input_values.push($("#form_input_question").val());
	i += 1
	$("#asked_question").append('<li class="list-unstyled">- ' + input_values[i] + '</li>');
};

function test_rotation(){
	const icon = $("#loading_icon")
	if(icon.css("display", "none")){
		icon.css("display", "block");
	}
	else{
		icon.css("display", "none");
	}
	if(icon.css("animation-play-state", "paused")){
		icon.css("animation-play-state", "running");
	}
	else{
		icon.css("animation-play-state", "paused");
	}
	setTimeout(() => {
	icon.css("animation-play-state", "paused");
	icon.css("display", "none");
    }, 3000);
}