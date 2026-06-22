const API_URL = "http://127.0.0.1:8000/articulos"

async function ObtenerArticulos() {
    try {
        const respuesta = await fetch(API_URL)
        const datos = await respuesta.json();

        document.getElementById("pantalla").textContent = JSON.stringify(datos, null, 2);
    } catch (error) {
        console.error("Error al obtener articulos", error);
    }
}