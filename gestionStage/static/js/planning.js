function submitAjax(idForm, urlTraitement, fonctionOK){
	$(idForm).submit( function(e) {
		console.log('envoi du form : ' + idForm)
		e.preventDefault(); // on empeche l'envoi du formulaire par le navigateur
		var datas = $(this).serialize();
		$.ajax({
			url: urlTraitement,
			data: datas,
			type: 'POST'
		}).done(function(data, textStatus, jqXHR){
			fonctionOK(data);
		}).fail(function(jqXHR, textStatus, errorThrown){
			console.log("ajax failed");
			alert(errorThrown);
		});
		return false;
	});
}

function extractDateHeure(arg){
	console.log("création Object date depuis String");
	console.log(arg);
	var dateTab = arg.split('T')[0];
	var dateHeure = arg.split('T')[1];

	dateTab = dateTab.split('-');
	dateHeure = dateHeure.split(':');

	return new Date(dateTab[0], dateTab[1] - 1, dateTab[2],
		dateHeure[0], dateHeure[1]);
}

function extractData(value){
	console.log('extraction données depuis : ');
	console.log(value);
	
	var debut = extractDateHeure(value['fields']['datePassage']);
	var fin = extractDateHeure(value['fields']['dateFinPrevu']);

	var res = {
		title: value['fields']['salle'],
		start: debut,
		end: fin,
		// la racine par du module !
		url: './' + value['pk'],
		allDay: false
	};
	console.log(res);
	return res;
}

function extractSoutenanceCalendarData(datas){
	var res = [];
	console.log('extraction des données depuis json');
	$.each(datas, function(index, value){
		res[index] = extractData(value);
	})
	console.log('données extraites :');
	console.log(res);
	return res;
}

function makeCalendar(donnees){
	var calendar = $('#planning').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		selectable: true,
		selectHelper: true,
		select: function(start, end, allDay) {
			$('#id_datePassage').val(start.toLocaleFormat("%Y-%m-%d %H:%M"));
			$('#id_dateFinPrevu').val(end.toLocaleFormat("%Y-%m-%d %H:%M"));
			$('#createSoutenance').click();
			calendar.fullCalendar('unselect');
		},
		editable: true,
		events: donnees,
		eventClick: function(event) {
			window.open(event.url);
            return false;
		}
	});
}

function updatePlanning(){
	$('#planning').html("");
	$.ajax({
		url: "./find/",
		data: {
			'dateD': $("#id_dateDebut").val(),
			'dateF': $("#id_dateFin").val()
		},
		type: 'GET',
		dataType: 'json',
		contentType: 'application/json'
	}).done(function(data, textStatus, jqXHR){
		$('#planning').html();
		makeCalendar(extractSoutenanceCalendarData(data));
	}).fail(function(jqXHR, textStatus, errorThrown){
		console.log("ajax failed");
		alert(errorThrown);
	});
}

function testArgs(){
	var deb = new Date($('#id_dateDebut').val());
	var fin = new Date($('#id_dateFin').val());
	if( deb >= fin ){
		alert('un début plus tard ou équivalent à une fin ... !');
		return false;
	} else {
		return true;
	}
}