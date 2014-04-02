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

function updateSoutenance(event){
	$.ajax({
		url: "./modifier/" + event.url.split('/')[event.url.split('/').length - 1],
		data: { },
		type: 'GET',
		dataType: 'html',
		contentType: 'application/html'
	}).done(function(data, textStatus, jqXHR){
		$('body').append(
			$('<form action="" method="post" id="tmp_modif"></form>').html(
				data
				.split('<form action="" method="post">')[1]
				.split('</form>')[0]));

		becomeDateTimePicker('#tmp_modif  #id_datePassage');
		becomeDateTimePicker('#tmp_modif #id_dateFinPrevu');

		$('#tmp_modif #id_datePassage').attr('value',
			event.start.toLocaleFormat("%Y-%m-%d %H:%M"));
		if(event.end == null || event.end == undefined){
			$('#tmp_modif #id_dateFinPrevu').attr('value',
				event.start.toLocaleFormat("%Y-%m-%d %H:%M"));
		} else {
			$('#tmp_modif #id_dateFinPrevu').attr('value',
				event.end.toLocaleFormat("%Y-%m-%d %H:%M"));
		}
		console.log('les nouvelles dates pour la soutenance ' +
			event.url.split('/')[event.url.split('/').length - 1] +
			' sont :');
		console.log($('#tmp_modif #id_datePassage').val());
		console.log($('#tmp_modif #id_dateFinPrevu').val());

		submitAjax("#tmp_modif",
			"./modifier/" + event.url.split('/')[event.url.split('/').length - 1],
			function(data){
				return;
			});

		$('#tmp_modif').submit();
		$('#tmp_modif').remove();
	}).fail(function(jqXHR, textStatus, errorThrown){
		console.log("ajax failed");
		alert(errorThrown);
	});
}

function makeCalendar(donnees, canSelect){
	var calendar = $('#planning').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		selectable: canSelect,
		selectHelper: canSelect,
		select: function(start, end, allDay) {
			if(canSelect){
				$('#id_datePassage').val(start.toLocaleFormat("%Y-%m-%d %H:%M"));
				$('#id_dateFinPrevu').val(end.toLocaleFormat("%Y-%m-%d %H:%M"));
				$('#createSoutenance').click();
				calendar.fullCalendar('unselect');
			}
		},
		editable: canSelect,
		eventDragStop: function( event, jsEvent, ui, view ){
			if(canSelect){
				updateSoutenance(event);
			}
		},
		eventResizeStop: function( event, jsEvent, ui, view ){
			if(canSelect){
				updateSoutenance(event);
			}
		},
		events: donnees,
		eventClick: function(event) {
			window.open(event.url);
            return false;
		}
	});
}

function updatePlanning(canSelect){
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
		makeCalendar(extractSoutenanceCalendarData(data), canSelect);
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