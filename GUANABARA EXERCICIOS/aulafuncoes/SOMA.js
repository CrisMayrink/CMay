num = 15;

function somar(num){
    
    var total = 0;
    for (var x = 0; x< num; x++){
        total += x;
    }
    return total;
}
console.log(somar(num)); 