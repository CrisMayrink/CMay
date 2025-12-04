/* OBS se nnão forem definidos todos os elementos n1 e n2, a função retorrna NaN - não é um número. Para resolver isso
é necessário deixar definida uma opção, parametros pré-definido, para o caso de falta de parâmetro n1=0 e n2=0*/
function soma( n1=0,n2=0){
    return n1 + n2
}
console.log(soma(2)) /*parametro definido na chamada da função soma 2,0 pq ele usou parametros opcionais*/

