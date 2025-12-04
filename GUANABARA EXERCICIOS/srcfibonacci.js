'use strict';

const executarBtn = document.getElementById("executar");
const limparBtn = document.getElementById("limpar");


executarBtn.addEventListener("click", gerarFibonacci, false);
limparBtn.addEventListener("click", limpar, false)

function gerarFibonacci(e) {
    
    const raw = document.getElementById("numero").value;
    const resp = document.getElementById("resp");
    const n = Number(raw);
    if(!Number.isFinite(n) || n<=0){
        alert("Digite um número maior que zero.");
        return;
    } if (n >100) {
        alert("Número muito grande. Digite um número menor que 100.");
        return;
    }
        const seq = [];
        let a = 0, b = 1;
        for (let i = 0; i < n; i++) {
            seq.push(b);
            const next = a + b;
            a = b;
            b = next;
        }
        resp.textContent = seq.join(", ");
}
function limpar(e) {
    document.getElementById("numero").value = "";
    document.getElementById("resp").textContent = "";
}



/*const fibonacci = (X) => {
    if (X == 0 || X === 1) return 1;
    let fm1 = 1, fm2=1, fm;
    for (let i=2; i<=X; i++){
        fm = fm1 = fm2;
        fm2 = fm1;
        fm1 = fm;
    }
    return fm;
}
const fiboRec = (x) => {
    return (x==0 || x==1) ? 1 : (fiboRec(x-1) + fiboRec(x-2));
}*/



