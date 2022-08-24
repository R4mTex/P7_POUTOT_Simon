function script(){
	if($("#form_input_question").val() != ""){
		change_text_send_button()
		send_request()
		icon_loading_rotation()
		show_history_bloc()
		show_history_input()
		initMap()
	}
	else{
	}
};

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

function show_history_input(){
	$("#GrandPyApp_response").remove()
	let input = $("#form_input_question").val()
	$("#history_question").append('<li class="list-unstyled">- ' + input + '</li>');
	setTimeout(() => {
		if(input == "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"){
			$("#history_question").append('<li class="list-unstyled" name="GrandPyApp_response">* Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris.</li>');
			setTimeout(() => {
				$("#grandpyapp_comments").append("<p id='GrandPyApp_response' name='GrandPyApp_response'>Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " +
				"La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. " +
				"Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse.</p>");
			}, 4500);
		}
	}, 2000);
};

function icon_loading_rotation(){
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

function initMap(){
    const test = $("#map")
	test.css("display", "none");

	setTimeout(() => {
        if(test.css("display", "none")){
		    test.css("display", "block");
	    }
	    else{
		    test.css("display", "none");
	    }
    }, 3000);

	let options = {
		zoom: 11,
		center: { lat: 48.8863155, lng: 2.3661888 }
	}

	let map = new google.maps.Map(document.getElementById('map'), options);

	let marker = new google.maps.Marker({
		position: { lat: 48.8863155, lng: 2.3661888 },
		map: map
	});

	let infoWindow = new google.maps.InfoWindow({
		content: "<h4>OpenClassRooms</h4>" +
		         "<h5>7 cité Paradis, 75010 Paris</h5>"
	         
	});

	marker.addListener('click', function(){
		infoWindow.open(map, marker);
	});
};
