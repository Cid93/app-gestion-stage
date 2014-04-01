$( document ).ready( function() {
    jQuery(function($){
        $.datepicker.regional['fr'] = {
            closeText: 'Fermer',
            prevText: '&#x3c;Préc',
            nextText: 'Suiv&#x3e;',
            currentText: 'Courant',
            monthNames: ['Janvier','Février','Mars','Avril','Mai','Juin',
            'Juillet','Août','Septembre','Octobre','Novembre','Décembre'],
            monthNamesShort: ['Jan','Fév','Mar','Avr','Mai','Jun',
            'Jul','Aoû','Sep','Oct','Nov','Déc'],
            dayNames: ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'],
            dayNamesShort: ['Dim','Lun','Mar','Mer','Jeu','Ven','Sam'],
            dayNamesMin: ['Di','Lu','Ma','Me','Je','Ve','Sa'],
            weekHeader: 'Sm',
            dateFormat: 'yy-mm-dd',
            firstDay: 1,
            isRTL: false,
            showMonthAfterYear: false,
            yearSuffix: ''};
        $.datepicker.setDefaults($.datepicker.regional['fr']);
    });
});

function becomeDateTimePicker(selecteurElement){
	$( selecteurElement ).datetimepicker({
        changeMonth: true,
        changeYear: true,
        format:'Y-m-d H:i'
    });
}

function becomeDatePicker(selecteurElement){
    $( selecteurElement ).datepicker();
    $( selecteurElement ).datepicker("option", "showAnim", "slide");
    $( selecteurElement ).datepicker("option", "dateFormat", "yy-mm-dd");
}

function publierBoutonAjouter(selecteurElement, addPath){
    $(selecteurElement)
        .parent()
        .append('<a style="padding:2px 7px;" class="btn btn-default" href="'
            + addPath
            + '">Ajouter</a>');
}

// NB : ajouter est la fonction appelé avant la fermeture du dialogue
function genDialogForm(selecteurTarget, selecteurBouton, largeur, hauteur, ajouter){
    console.log("mise en .dialog de " + selecteurTarget);
    $(selecteurTarget).dialog({
        autoOpen: false,
        height: hauteur,
        width: largeur,
        modal: true,
        buttons: {
            "Valider": function(){
                ajouter();
                $( this ).dialog( "close" );
            },
            "Annuler": function() {
                $( this ).dialog( "close" );
            }
        },
        close: function() {
            $( this ).dialog( "close" );    
        }
    });
    console.log(selecteurTarget + ' activé sur click de ' + selecteurBouton);
    $(selecteurBouton).click(function(){
        $(selecteurTarget).dialog( "open" );
    });
}

// NB : ajouter est la fonction appelé avant la fermeture du dialogue
// depuis genDialogForm
function publierBoutonAjouterDialog(selecteurElement, boutonId, formId, largeur, hauteur, ajouter){
    console.log(selecteurElement + ' va être suivi d\'un bouton ' + boutonId);
    $(selecteurElement)
        .parent()
        .append('<a id="'+ boutonId.split('#')[1] + '" href="#" style="padding:2px 7px;" class="btn btn-default">Ajouter</a>');
    genDialogForm(formId, boutonId, largeur, hauteur, ajouter);
}

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