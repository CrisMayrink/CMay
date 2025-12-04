'use strict';

const numeros = [];
const inputNumero = document.getElementById('numero');
const btnAdicionar = document.getElementById('btnAdicionar');
const btnFinalizar = document.getElementById('btnFinalizar');
const res = document.getElementById('res');   

if (inputNumero && btnAdicionar && btnFinalizar && res) {
    btnAdicionar.addEventListener('click', adicionar, false);
    btnFinalizar.addEventListener('click', finalizar, false);
    inputNumero.addEventListener('keydown', (e) => { if (e.key === 'Enter') adicionar(); });
} else {
    console.error('Elementos não encontrados no DOM.');
}
function atualizarLista() {
    res.textContent = numeros.length ? `Números adicionados: ${numeros.join(', ')}` : 'Números adicionados: nenhum';
}
function adicionar() {
    const raw = inputNumero.value;
    const n = Number(raw);
    

    if (!Number.isFinite(n) || !Number.isInteger(n)) {
        alert('Digite um número inteiro válido.');
        inputNumero.focus();
        return; //exceção de segurança
    }
    if (n < 1 || n > 50) {
        alert('Digite um número entre 1 e 50.');
        inputNumero.focus();
        return;
    }
    if (numeros.includes(n)) {
        alert('Número já adicionado.');
        inputNumero.value = '';
        inputNumero.focus();
        return;
    }
     numeros.push(n);
    atualizarLista();
    inputNumero.value = '';
    inputNumero.focus();
}

function finalizar(){
    if (numeros.length === 0) {
        alert('Adicione valores antes de finalizar.');
        return;
    }

    const sorted = [...numeros].sort((a, b) => a - b);
    const maior = Math.max(...numeros);
    const menor = Math.min(...numeros);
    const soma = numeros.reduce((acc, v) => acc + v, 0);
    const media = soma / numeros.length;

    res.innerHTML = `
        Foram adicionados <strong>${numeros.length}</strong> valores. <br>
        Valores (ordenados): ${sorted.join(', ')} <br>
        Maior: <strong>${maior}</strong><br>
        Menor: <strong>${menor}</strong><br>
        Média: <strong>${media.toFixed(2)}</strong>    
    
    `;
}

        