const url = 'https://randomuser.me/api/?results=10';

async function getUsers(retorno){
    try{
        const resp= await fetch(url);
        const objeto= await resp.json();
        
        let itens= "";
        for(let pessoa of objeto.results){
            itens += `<li>${pessoa.name.first} ${pessoa.name.last}</li>`
        }
        document.getElementById(retorno).innerHTML= itens;
    } catch (error) {
        console.error("Ocorreu um erro ao buscar os usuários:", error);
        document.getElementById(retorno).innerHTML = "<li>Erro ao carregar dados.</li>";
    }
}


