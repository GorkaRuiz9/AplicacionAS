const express = require('express');
const fs = require('fs');
const path = require('path');
require('dotenv').config(); // para cargar .env si lo usas

const app = express();
const PORT = 3000;

// --- Servir estáticos ---
app.use(express.static(path.join(__dirname, 'public')));

// --- Función para servir HTML con reemplazo dinámico ---
function sendHtmlWithEnv(res, fileName) {
  const filePath = path.join(__dirname, 'views', fileName);
  let html = fs.readFileSync(filePath, 'utf-8');
  html = html.replace(/__API_URL__/g, process.env.API_URL || 'http://localhost:8000');
  res.send(html);
}

// --- Rutas HTML --- (Se cambia el valor de la url de la API por la variable de entorno)
app.get('/', (req, res) => sendHtmlWithEnv(res, 'index.html'));
app.get('/items', (req, res) => sendHtmlWithEnv(res, 'items.html'));
app.get('/favoritos', (req, res) => sendHtmlWithEnv(res, 'favoritos.html'));

// --- Lanzar servidor ---
app.listen(PORT, () => {
  console.log(`🌍 Servidor corriendo en http://localhost:${PORT}`);
  console.log(`Usando API_URL=${process.env.API_URL}`);
});
