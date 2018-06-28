function truncateString(str, length) {
   return str.length > length ? str.substring(0, length - 3) + '...' : str
}

function checkExp(valor){
    var expreg = new RegExp("[^-_a-zA-Z 0-9./]+");
    return !expreg.test(valor);
}