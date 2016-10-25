$('document').ready(function(){
    var itemsPerPage = 6;
    var numeroProgramas = $('#numeroProgramas').text();
    var totalPages = Math.ceil(numeroProgramas/itemsPerPage);
    
    // console.log("Cantidad de programas: "+numeroProgramas);
    addNumberPagination(totalPages);
    switchPage("1",numeroProgramas,itemsPerPage);
    
    
    
    /*if($('li[data-page="1"]').hasClass('active') && numeroProgramas > 6)
    {
        for (i = numeroProgramas; i>6; i--) {
            $('div[data-cual="'+i+'"]').addClass("hidden");
        }
    }*/
    
    // Capturar clics en numeros de paginacion
    $('.thePagination').on('click', function(e){
        e.preventDefault();
        var what = $(this).data('page');
        // console.log('page clicked: ', what);
        // Animacion para que suba hasta el breadcumb
        $('html, body').animate({scrollTop : 110},800);
        // $(window).scrollTop(110);
        // var position = $(window).scrollTop();
        // console.log('position: '+position);
        switchPage(what, numeroProgramas, itemsPerPage);
        setActivePage(what, totalPages);
    });
    
});
// Mostrar y ocultar programas segun corresponda
function switchPage(pageAt, numeroProgramas, itemsPerPage){
    // Ocultar todos los programas
    for (i = numeroProgramas; i > 0; i--) 
    {
        $('div[data-cual="'+i+'"]').addClass("hidden");
        // console.log('div[data-cual="'+i+'"]');
    }
    
    // Definir que programas mostrar
    var start = (pageAt-1)*itemsPerPage;
    var end = pageAt*itemsPerPage;
    if (end > numeroProgramas)
    {
        end = numeroProgramas;
    }
    // console.log('start:'+start+' end:'+end);
    
    // Mostrar programas definidos
    for (i = end; i > start; i-- )
    {
        $('div[data-cual="'+i+'"]').removeClass("hidden");
    }
}
// Definir cual es la pagina activa en la paginacion inferior
function setActivePage(pageAt, totalPages)
{
    // console.log('total pages: '+totalPages);
    for (i = totalPages; i > 0; i--)
    {
        $('a[data-page="'+i+'"]').parent().removeClass();
    }
    $('a[data-page="'+pageAt+'"]').parent().addClass('active');
}
// Agregar numeracion segun la cantidad de programas
function addNumberPagination(totalPages)
{
    console.log('adding...');
    for (i = 2; i <= totalPages; i++)
    {
        $('.pagination').append('<li><a class="thePagination" data-page="'+i+'" href="#">'+i+'</a></li>');
        
    }
    
}
