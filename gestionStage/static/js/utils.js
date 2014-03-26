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