function extractSoutenanceCalendarData(datas){
	var res = [];
	console.log('extraction des données depuis json');
	$.each(datas, function(index, value){
		var dateTab = value['fields']['datePassage'].split('T')[0];
		var dateHeure = value['fields']['datePassage'].split('T')[1];

		dateTab = dateTab.split('-');
		dateHeure = dateHeure.split(':');

		var debut = new Date(dateTab[0], dateTab[1] - 1, dateTab[2],
			dateHeure[0], dateHeure[1]);

		res[index] = {
			title: value['fields']['salle'],
			start: debut,
			end: new Date(debut.getTime() + 35*60000),
			// la racine par du module !
			url: './' + value['pk'],
			allDay: false
		}
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
			var title = prompt('Event Title:');
			if (title) {
				calendar.fullCalendar('renderEvent',
					{
						title: title,
						start: start,
						end: end,
						allDay: allDay
					},
					true // make the event "stick"
				);
				creerSoutenance(title);
			}
			calendar.fullCalendar('unselect');
		},
		editable: true,
		events: donnees
	});
}

function updatePlanning(){
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