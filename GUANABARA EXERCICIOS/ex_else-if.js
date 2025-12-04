const num1 = 2;
const num2 = -15;

if (num1 > num2 && num2 > 0){
    console.log("A primeira variável é maior que a segunda e a segunda é um número positivo.");
} else if (num1 > num2 && num2 <=0){
    console.log("a primeira variavel é maior que a segunda e a segunda variável não é um número positivo.");
} else if(num1 < num2 || num2 > 0 ){
    console.log("A primeira variável é menor que a segunda ou a segunda variável é um numero positivo.");    
} else {
    console.log("Nenhuma das condições anteriores foram atendidas.");
}



