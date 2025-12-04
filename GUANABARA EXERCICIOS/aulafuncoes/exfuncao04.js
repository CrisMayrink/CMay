/*calcular o fatorial de um número 5!(fatorial) = 5x4x3x2x1 = 120 - TRADICIONAL*/

/*function fatorial(n){
    let fat= 1
    for(let c = n; c >1; c -- ){ //o contador c começa em n e eqto for maior q 1 vou subtrair 1
        fat *= c //depois multiplica fatorial (5,4,3,2,1) x c
    }
}
    return fat*/

//RECURSIVIDADE OUTRA FORMA

function fatorial (n){ /*estou criando uma função fatorial que dentro dela tem uma chamada pra ela mesma*/
    if (n==1) {
        return 1
    } else {
        return n * fatorial(n-1) //chamada pra ela mesma
    }
}

console.log(fatorial(5))
