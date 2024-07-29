const API_BASE_URL = 'https://tudominio.render.com';

async function consultarCantidadMes() {
    const mes = document.getElementById('mes-input').value.toLowerCase();
    const response = await fetch(`${API_BASE_URL}/cantidad_peliculas_mes/${mes}`);
    const data = await response.text();
    document.getElementById('cantidad-mes-resultado').innerText = data;
}

async function consultarCantidadDia() {
    const dia = document.getElementById('dia-input').value.toLowerCase();
    const response = await fetch(`${API_BASE_URL}/cantidad_peliculas_dia/${dia}`);
    const data = await response.text();
    document.getElementById('cantidad-dia-resultado').innerText = data;
}

async function consultarScoreTitulo() {
    const titulo = document.getElementById('titulo-score-input').value;
    const response = await fetch(`${API_BASE_URL}/score_titulo/${titulo}`);
    const data = await response.json();
    document.getElementById('score-titulo-resultado').innerText = JSON.stringify(data);
}

async function consultarVotosTitulo() {
    const titulo = document.getElementById('titulo-votos-input').value;
    const response = await fetch(`${API_BASE_URL}/votos_titulo/${titulo}`);
    const data = await response.json();
    document.getElementById('votos-titulo-resultado').innerText = JSON.stringify(data);
}

async function consultarActor() {
    const actor = document.getElementById('actor-input').value;
    const response = await fetch(`${API_BASE_URL}/get_actor/${actor}`);
    const data = await response.json();
    document.getElementById('actor-resultado').innerText = JSON.stringify(data);
}

async function consultarDirector() {
    const director = document.getElementById('director-input').value;
    const response = await fetch(`${API_BASE_URL}/get_director/${director}`);
    const data = await response.json();
    document.getElementById('director-resultado').innerText = JSON.stringify(data);
}

async function getRecomendaciones() {
    const titulo = document.getElementById('titulo-recom-input').value;
    const response = await fetch(`${API_BASE_URL}/recomendacion_m1/${titulo}`);
    const data = await response.json();
    document.getElementById('recomendaciones-resultado').innerText = data.join(', ');
}
