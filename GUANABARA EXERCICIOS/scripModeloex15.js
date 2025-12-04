function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >=0 && idade < 10) {
                //Criança
                img.setAttribute('src', 'menino5anos.png')
            } else if (idade < 21) {
                //Jovem
                img.setAttribute('src', 'homem15anos.png')
            } else if (idade < 32) {
                //Jovem
                img.setAttribute('src', 'homem25anos.png')
            } else if (idade <59) {
                //Adulto
                img.setAttribute('src', 'homem35anos.png')
            } else {
                //Idoso
                img.setAttribute('src', 'homem65anos.png')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'  
            if (idade >=0 && idade < 10) {
                //Criança
                img.setAttribute('src', 'menina5anos.png')
            } else if (idade < 21) {
                //Jovem
                img.setAttribute('src', 'mulher15anos.png')
            } else if (idade < 32) {
                //Jovem
                img.setAttribute('src', 'mulher25anos.png')
            } else if (idade <59) {
                //Adulta
                img.setAttribute('src', 'mulher45anos.png')
            } else {
                //Idosa 
                img.setAttribute('src', 'mulher65anos.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}