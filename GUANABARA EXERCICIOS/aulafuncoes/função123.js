function faz (n){
s = n.toString();
variavel = 0;
for (c of s){
    d = parseInt(c);
    variavel += d;
    }
    return variavel;
}
resultado = faz(123123);
console.log("Resultado: ", resultado);
