$(document).ready(function() {

    var dialog, form
    var lang = $('html').attr('lang');
      emailRegex = /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
      email = $( "#email" ),
      allFields = $( [] ).add( email ),
      tips = $( ".validateTips" );

      function updateTips( t ) {
      tips
        .text( t )
    }
    function checkLength( o, n, min, max ) {
      if ( o.val().length > max || o.val().length < min ) {
        updateTips( "Length of " + n + " must be between " +
          min + " and " + max + "." );
        return false;
      } else {
        return true;
      }
    }

    function checkRegexp( o, regexp, n ) {
      if ( !( regexp.test( o.val() ) ) ) {
        updateTips( n );
        return false;
      } else {
        return true;
      }
    }

    function addInvite() {
      var valid = true;
      allFields.removeClass( "ui-state-error" );
      valid = valid && checkLength( email, "email", 6, 80 );
      valid = valid && checkRegexp( email, emailRegex, "eg. ui@jquery.com" );
      if ( valid ) {
        $.ajax({
            method: "POST",
            url: '/invite/',
            data: {
            'email': email.val(),
            'csrfmiddlewaretoken': CSRF_TOKEN,
            'language':lang
            },
            success: function(response, status) {
              alert(response['msg']);
              dialog.dialog( "close" );
                },
            error: function(response) {
              alert("Error");
              dialog.dialog( "close" );
            }
          });
      }
      return valid;
    }

    dialog = $( "#dialog" ).dialog({
      position: { my: "center bottom", at: "center center", of: window },
      autoOpen: false,
      modal: true,
      resizable: false,
      buttons: {
        "Invite your friend": addInvite
      },
    });

    form = dialog.find( "form" ).on( "submit", function( event ) {
      event.preventDefault();
      addInvite();
    });
    $( "#opener" ).button().on( "click", function() {
      dialog.dialog( "open" );
    });
})
