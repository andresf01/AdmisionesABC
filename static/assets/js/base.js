$('document').ready(function(){
    
    // Set red line 
    var myLocation = window.location.href;
    console.log('location: '+myLocation);
    var directories = myLocation.split("/");
    var page = directories[directories.length - 2];
    console.log('located in: '+page);
    $('#b_'+page).addClass('active');
    if (page == 'admisionesabc-andresf01.c9users.io')
    {
        $('#b_').addClass('active');
    }
    //admisionesabc-andresf01.c9users.io
    
});