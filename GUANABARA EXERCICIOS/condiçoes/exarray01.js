const num = [5,8,2,9,3]
num.push(7);               // adiciona antes de ordenar, se quiser 7 na ordenação final
num.sort((a, b) => a - b); // ordenação numérica

console.log(`Esse é o nosso vetor [${num}].`)
console.log(`Nosso vetor tem ${num.length} posições.`)
console.log(`O valor do vetor posição 2 é ${num[2]}.`)
posição= 0

for(let posicao=0; posicao<num.length; posicao++){
    console.log(`Posição ${posicao}: ${num[posicao]}`);
}
