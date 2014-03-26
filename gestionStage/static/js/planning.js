const tab = "#table_planning";
const theadTab = "#entete_planning";
const bodyTab = "#body_planning";
const saveTableau = $(tab).html();

const tabJ = "#table_planningJ";
const theadTabJ = "#entete_planningJ";
const bodyTabJ = "#body_planningJ";
const saveTableauJ = $(tabJ).html();

const  month=new Array();
month[0]="Janvier";
month[1]="Février";
month[2]="Mars";
month[3]="Avril";
month[4]="Mai";
month[5]="Juin";
month[6]="Juillet";
month[7]="Août";
month[8]="Septembre";
month[9]="Octobre";
month[10]="Novembre";
month[11]="Decembre";

function reinitTableaux(theTableau, savedTableau){
	console.log('réinitialisation du planning : ' + theTableau);
	$(theTableau).html(savedTableau);
	console.log('planning réinitialisé : ' + theTableau);
}

function getListeSalles(listeSoutenance){
	var salles = [];
	console.log('récupération des salles');
	$.each(listeSoutenance, function(index, value){
		if($.inArray(value['fields']['salle'], salles) == -1){
			console.log('nouvelles salles : ' + value['fields']['salle']);
			salles.push(value['fields']['salle']);
		}
	});
	salles.sort();
	console.log(salles);
	return salles;
}

function putTheadTabbleau(theTableauEntete, listeSoutenance){
	console.log('création de l\'entête du tableau : ' + theTableauEntete);
	var cellules = [];
	$.each(getListeSalles(listeSoutenance), function(index, value){
		$(theTableauEntete).append($('<td>' + value + '</td>'));
	});
	console.log('entête faite : ' + theTableauEntete);
}

function addHeaders(firstLine, deb, end, months){
	var i = new Date(deb);
	$.each($(firstLine + ' td'), function(index, value){
		if(index != 0){
			$(value).html($(value).html() + ' '
				+ i.getDate() + ' ' + months[i.getMonth()]);
			i.setDate(i.getDate() + 1);
		}
	});
}

function identifierCellule(selecteurTbody, listeSoutenance){
	console.log('mise en place des id sur chaque td');
	var nbDeSalles = getListeSalles(listeSoutenance).length;
	console.log(nbDeSalles + ' colonnes par lignes');
	var ptDeDepart = $(selecteurTbody + ' tr:nth-child(2)');
	// l'index commencera à 1 donc on le compence avec ptDeDepart
	ptDeDepart = ptDeDepart.attr('id').split("_")[1] - 1;
	var firstLoop = true;
	$.each($(selecteurTbody + ' tr'), function(index, value){
		if( ! firstLoop){
			for ( var i = 0; i < nbDeSalles; i++ ) {
				$(this).append('<td id="l_' + (parseInt(ptDeDepart) + index) + '_c_' + i + '"></td>')
				console.log('généré : <td id="l_' + (parseInt(ptDeDepart) + index) + '_c_' + i + '"></td>')
			}
		}
		firstLoop = false;
	});
}

function getCelluleCompletee(informationsStage){
	var infoEtu = informationsStage['etudiant']['prenom'] + 
		' ' + 
		informationsStage['etudiant']['nom'];
	var infoEnt = informationsStage['entreprise']['nom'];
	var infoMDS = informationsStage['enseignantTuteur']['prenom'] +
		' ' +
		informationsStage['enseignantTuteur']['nom'];
	console.log('infos sur le stage :');
	console.log(infoEtu);
	console.log(infoEnt);
	console.log(infoMDS);

	var res = '<a href="./' + informationsStage['id'] + '" target="_blank">' +
		infoEtu + ' chez ' +
		infoEnt + '<br />avec "' + infoMDS + '"</a>';
	console.log(res);
	return res;
}

function remplirTableauxJ(bodyTab, data){
	var salles = getListeSalles(data);
	$.each(data, function( index, value ) {
		var heure = value['fields']['datePassage']
			// recuperation de l'heure et minutes
			.split("T")[1]
			// recuperation seule de l'heure
			.split(":")[0];

		var salle = 0;
		for(i = 0; i < salles.length; i++){
			if(value['fields']['salle'] == salles[i]){
				salle = i;
			}
		}

		// recherche de l'id de la cellule cible
		var target = '#l_' + heure + '_c_' + salle;

		console.log('soutenance sur ' + target);
		$(target).html(
			getCelluleCompletee(
				value['fields']['stage']));
	});
}

function remplirTableaux(bodyTab, data){
	$.each(data, function( index, value ) {
		var heure = value['fields']['datePassage']
			// recuperation de l'heure et minutes
			.split("T")[1]
			// recuperation seule de l'heure
			.split(":")[0];

		var laDate = value['fields']['datePassage']
			// recuperation de la date sans l'heure
			.split('T')[0]
			// mise en tableau de l'année, mois, jour
			.split('-');
		var jour = new Date(laDate[0], laDate[1] - 1, laDate[2]).getDay();

		// recherche de l'id de la cellule cible
		var target = '#l_' + heure + '_d_' + jour;

		console.log('soutenance sur ' + target);
		$(target).html($(target).html() + value['fields']['salle']);
	});
}