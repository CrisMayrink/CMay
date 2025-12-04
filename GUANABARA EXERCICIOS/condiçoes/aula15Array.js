let num = [5,8,2,9,3]
num.sort()
num.push(7)
console.log(`Esse é o nosso vetor [${num}].`)
console.log(`Nosso vetor tem ${num.length} posições.`)
console.log(`O valor do vetor posição 2 é ${num[2]}.`)
/* um jeito mais simples de fazer o FOR para array = FOR IN.
usando vetor.index() ele busca o VALOR não o índice, dentro das chaves
for(let posicao=0; posicao<num.length; posicao++){
    console.log(`A posição ${posicao} tem valor ${num[posicao]}`)
}*/
let posicao = num.indexOf(10)
if (posicao == -1){
    console.log('O valor não foi encontrado!')
} else {
    console.log(`O valor está na posição ${posicao}`)
}
/*for( let posicao in num){
    console.log(`A posição ${posicao} tem o valor ${num[posicao]}`)
}*/