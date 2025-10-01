// 1. Pega o elemento da imagem usando o ID
const imagem = document.getElementById('Logo html')
// 2. Adiciona um "ouvinte de evento" para o clique
imagem.addEventListener('click', function() {
    // 3. Quando o clique ocorrer, redireciona para a URL desejada
    window.location.href = 'https://pt.wikipedia.org/wiki/HTML';
});