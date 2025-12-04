const url = 'https://dummyjson.com/products/?limit=10';

async function getUsers(retorno){
    try{
        const resp= await fetch(url);
        const objeto= await resp.json();
        
        let itens= "";
        for(let products of objeto.products){
            itens += `<li>${products.title} ${products.price}</li>`
        }
        document.getElementById(retorno).innerHTML= itens;
    } catch (error) {
        console.error("Ocorreu um erro ao buscar os usuários:", error);
        document.getElementById(retorno).innerHTML = "<li>Erro ao carregar dados.</li>";
    }
}


