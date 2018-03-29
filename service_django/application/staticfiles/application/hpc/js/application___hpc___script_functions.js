function truncateString(str, length) {
   return str.length > length ? str.substring(0, length - 3) + '...' : str
}

function insertMessage(status, message){
   if(status=='error')
       $('#content').prepend('<div id="message-error" class="alert alert-danger" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Cerrar"><span aria-hidden="true">&times;</span></button><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>&nbsp;&nbsp;&nbsp;' + message + '</div>');
   if(status=='success')
       $('#content').prepend('<div id="message-success" class="alert alert-success" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Cerrar"><span aria-hidden="true">&times;</span></button><span class="glyphicon glyphicon-hand-right" aria-hidden="true"></span>&nbsp;&nbsp;&nbsp;' + message + '</div>');
   $("html, body").animate({scrollTop: 0}, 500);
}

function checkExp(valor){
    expreg = new RegExp("[^-_a-zA-Z 0-9./]+");
    return !expreg.test(valor);
}