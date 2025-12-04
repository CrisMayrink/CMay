'use strict';

const qtdeInteracoes = 2;
const numeros = [];



const inputNumeros = document.getElementById('numeros');
const btnAdicionar = document.getElementById('btnAdicionar');
const btnDividir = document.getElementById('btnDividir');
const btnLimpar = document.getElementById('btnLimpar');
const res = document.getElementById('res');  

if (inputNumeros && btnAdicionar && btnDividir && res) {
    btnAdicionar.addEventListener('click', adicionar, false);
    btnDividir.addEventListener('click', dividir, false);
    inputNumeros.addEventListener('keydown', (e) => { 
        if (e.key === 'Enter') {
            adicionar(); 
        }
    });   

    // Adiciona o listener para o botão Limpar (já que você tem o ID no HTML)
    const btnLimpar = document.getElementById('btnLimpar');
    if (btnLimpar) {
        btnLimpar.addEventListener('click', limpar, false);
    }

} else {
    console.error('Elementos não encontrados no DOM.');
}


function limpar() {
     // 1. Limpa o array principal de números
    numeros.length = 0; // Método eficiente para esvaziar o array mantendo a referência original

    // 2. Atualiza a exibição do resultado para o estado inicial
    atualizarLista(); 
    
    // 3. Limpa o campo de input e devolve o foco para o usuário digitar novamente
    inputNumeros.value = '';
    inputNumeros.focus();

    // 4. Reabilita o botão Adicionar, caso ele tenha sido desativado anteriormente
    btnAdicionar.disabled = false; 
}

function atualizarLista() {
    if (numeros.length === 0){
        res.innerHTML = '<li>Números adicionados: nenhum</li>';

    }else{
        const itensLista = numeros.map(numero => `<li>${numero}</li>`);
        res.innerHTML = itensLista.join('');
    }
     
}
function adicionar() {
    if (numeros.length >= qtdeInteracoes) {
        alert(`Você já adicionou ${qtdeInteracoes} números. Clique em "Dividir" para finalizar.`);
        inputNumeros.value = '';// limita o numero de entradas
        return; 
    }

    const raw = inputNumeros.value;
    const n = Number(raw);
    
    if (!Number.isFinite(n) || !Number.isInteger(n)) {
        alert('Digite um número inteiro válido.');
        inputNumeros.focus(); //devolve para o campo adicionar
        return; //exceção de segurança
    }
    if (n < 1 ) {
        alert('Digite um número inteiro positivo maior que 0.');
        inputNumeros.focus(); //devolve para inserir um numero válido
        return;
    }
    if (numeros.includes(n)) {  //limita numeros ja incluidos anteriormente
        alert('Número já adicionado.');
        inputNumeros.value = '';
        inputNumeros.focus(); //devolve para o campo adicionar
        return;
    }
    numeros.push(n);
    atualizarLista();
    inputNumeros.value = '';
    inputNumeros.focus();

    if (numeros.length >= qtdeInteracoes) {
        btnAdicionar.disabled = true; // desabilita o botao adicionar após a inserção dos numeros
    }
}
    
function dividir(){
    if (numeros.length <2) {
        alert('Adicione pelo menos dois valores antes de finalizar.');
        return;    //garante que dois numeros serão adicionados
    }
    const a = numeros[0]; // 1° numero dividendo
    const b = numeros[1]; //2° numero divisor
    
    if (b === 0) {
        alert('Divisão por zero não permitida.'); //verifica a divisão por zero antes de prosseguir
        return;
    }
    const divisao = a/b;

    res.innerHTML=
        `<li>Foram adicionados os números ${numeros.join(' e ')}.</li>
        <li> O resultado da divisão do primeiro número ${a} pelo segundo número ${b} é: <strong>${divisao.toFixed(2)}</strong>.</li>`;
}    
