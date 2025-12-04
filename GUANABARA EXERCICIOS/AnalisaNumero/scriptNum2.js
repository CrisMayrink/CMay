'use strict';
// escopo global 
let num = document.querySelector('input#fnum') //para a div fnum q recebe o num
let lista = document.querySelector('select#flista') //para a div lista
let res = document.querySelector('div#res')//para a div resultado
let valores = [] //valares adicionados - vetor

function isNumero(n){// verificar se é ou não numero
    if (Number(n) >=1 && Number(n) <=100){
        return true
    } else{
        return false
    }
}
function inLista(n, l){ //dois parametros o numero e a lista valores
    if (l.indexOf(Number(n)) != -1){  //se o n (-1) não foi encontrado na lista
        return true
    }else{
        return false
    }
}   
function adicionar(){
    if(isNumero(num.value) && !inLista(num.value, valores)){//só vai adicionar se for um numero isNumero e 
    //se não (!) estiver na lista valores, meu vetor- se nfor v adiciona
        valores.push(Number(num.value))  //push é adc um elemnto no vetor -se não está na lista adc o valor de num a valores
        let item = document.createElement('option') //cria um elemento na lista
        item.text= `Valor ${num.value} adicionado.` //mostra o valor adicionado
        lista.appendChild(item) //adciona o item na lista
        res.innerHTML = '' //pra limpar a lista anterior qdo adc elementos apos finalizar
    }else{
        window.alert('Valor inválido ou cadastrado na lista.')
    }
    num.value= ''; //limpa a lista apos adc
    num.focus() // volta o cursor pro campo adc
}
function finalizar(){
    if(valores.length == 0){ //verifica se tem valores dentro do vetor
        window.alert('Adicione valores antes de finalizar!')
    }else{
        let tot = valores.length
        let maior= valores[0]
        let menor= valores[0]

        let soma = 0
        let media = 0
        for(let pos in valores){ 
            soma += valores[pos]
            if(valores[pos] > maior)//bloco q verifica quem é o maior e menor
                maior =  valores[pos]
            if (valores[pos] < menor)
                menor = valores[pos]
        }
        media =  soma/tot
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo temos ${tot} números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi: ${maior}.</p>`
        res.innerHTML += `<p>O menor valor informado foi: ${menor}.</p>`
        res.innerHTML += `<p>A média dos valores digitados é ${media.toFixed(2)}.</p>`
    }
}
