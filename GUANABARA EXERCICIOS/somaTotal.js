'use strict';


let somaTotal = 0;
const qtdeInteracoes = 50;

const botao = document.getElementById('btnSomar');
const res = document.getElementById('res');

if (botao && res) {
    botao.addEventListener('click', somar, false);
} else {
    console.error('Elementos não encontrados no DOM.');
}//proteção se o botao ou o res forem null

function somar(){
    somaTotal = 0;
    for(let i = qtdeInteracoes; i >= 1; i--){
        somaTotal += i; //equivalente a usar somTotal = somaTotal = 1
    }
res.innerHTML = `A soma é igual a <strong>${somaTotal}</strong>.`//essa atribuição deve estar dentro da função somar()
}