// server.js
const express = require('express');
const path = require('path');
const { MongoClient } = require('mongodb');

const app = express();
const PORT = 3000;



// --- 🖼️ Servir archivos estáticos ---
app.use(express.static(path.join(__dirname, 'public')));

// --- 📄 Rutas HTML ---
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.get('/items', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'items.html'));
});

app.get('/favoritos', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'favoritos.html'));
});

// --- 🚀 Iniciar servidor ---
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
