// Funcion para animar la desaparicion de los mensajes
$.fn.slideFadeToggle  = function(speed, easing, callback) {
        return this.animate({opacity: 'toggle', height: 'toggle'}, speed, easing, callback);
}; 

function itemWithTimer(id, tiempo){
  $(id).show();
  setTimeout(function() { $(id).slideFadeToggle(); }, tiempo*1000);
}