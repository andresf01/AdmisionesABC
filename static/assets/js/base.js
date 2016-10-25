$('document').ready(function(){
    
    // Set red line script
    var directories = window.location.href.split("/");
    var page = directories[directories.length - 1];
    var i = 2;
    
    // While for find the app
    while( page == '' || page == '/')
        page = directories[directories.length - (i++)];
    
    // Message to confirm location   
    console.log('located in: '+page);
    
    // If my app is home
    if (page == 'admisionesabc-andresf01.c9users.io')
    {
        $('#b_').addClass('active');
    }
    // If the app is another
    else
    {
        $('#b_'+page).addClass('active');
    }
    
});