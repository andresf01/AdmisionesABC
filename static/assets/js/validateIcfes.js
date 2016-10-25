$('document').ready(function(){
    
    $('#submit').on('click',function(e){
        e.preventDefault();
        $.ajax({
            beforeSend: function(){
            },
            url: window.location.href+"/tiki",
            type: 'POST',
            data: {'id': '11223344', 'snp': 'ac21342098'},
            // headers:  {"X-CSRFToken": getCookie("csrftoken")},
            success: function(resp){
              // OK
              console.log('its ok');
            },
            error: function(jqXHR, estado, error){
                $('#errorMessage').removeClass('hidden');
                console.log('error');
            },
            complete: function(jqXHR, estado){
            },
            timeout: 10000
            
          });
    });
    
});