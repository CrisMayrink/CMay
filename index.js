var idade= 12
if (idade < 16) {
    console.log(`Com  ${idade} anos não vota.`)
} else if ((idade >=16 && idade <18) || idade >=65) {
    console.log(`Com  ${idade} anos o Voto é opcional.`)
} else {
    console.log(`Com ${idade} anos o Voto é obrigatório.`)
}
